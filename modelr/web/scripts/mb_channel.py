'''
Created on Apr 30, 2012

@author: Sean Ross-Ross, Matt Hall, Evan Bianco
'''
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from argparse import ArgumentParser
from modelr.web.defaults import default_parsers
from modelr.web.urlargparse import rock_properties_type

from modelr.web.util import modelr_plot

import modelr.modelbuilder as mb

from svgwrite import rgb

# This is required for Script help
short_description = 'Create a simple wedge model.'

def add_arguments(parser):
    default_parser_list = ['ntraces',
                           'pad',
                           'reflectivity_method',
                           'title',
                           'theta',
                           'f',
                           'colourmap',
                           'wavelet', 
                           'wiggle_skips',
                           'aspect_ratio',
                           'base1','base2','overlay1','overlay2',
                           'opacity'
                           ]
    
    default_parsers(parser,default_parser_list)
    
    parser.add_argument('Rock0',
                        type=rock_properties_type, 
                        help='Rock properties of upper rock '+
                        '[Vp,Vs, rho]',
                        required=True,
                        default='2000,1000,2200'
                        )
                        
    parser.add_argument('Rock1',
                        type=rock_properties_type, 
                        help='Rock properties of middle rock ' +
                        '[Vp, Vs, rho]',
                        required=True,
                        default='2200,1100,2300'
                        )
    
    parser.add_argument('Rock2',
                        type=rock_properties_type, 
                        help='Rock properties of lower rock ' +
                        '[Vp, Vs, rho]',
                        required=False,
                        default='2500,1200,2600'
                        )
    
    parser.add_argument('thickness',
                        default=50,
                        type=int,
                        help='The maximum thickness of the wedge'
                        )
                            
                        
    parser.add_argument('margin',
                        type=int,
                        help='Traces with zero thickness',
                        default=1
                        )

    parser.add_argument('slice',
                        type=str,
                        help='Slice to return',
                        default='spatial',
                        choices=['spatial', 'angle', 'frequency']
                        )
                        
    parser.add_argument('trace',
                        type=int,
                        help='Trace to use for non-spatial slice',
                        default=0
                        )
                        
    return parser

def run_script(args):
    from modelr.constants import dt, duration
    matplotlib.interactive(False)
    
    """if args.transparent == 'False' or args.transparent == 'No':
        transparent = False
    else:
        transparent = True"""
    transparent = False
    # This is a hack to conserve colors
    l1 = (150,110,110)
    l2 = (110,150,110)
    l3 = (110,110,150)
    layers= [l1,l2]
    colourmap = { rgb(150,110,110): args.Rock0,
                  rgb(110,150,110): args.Rock1 }
    
    if not isinstance(args.Rock2, str):
        colourmap[rgb( 110,110,150)] = args.Rock2
        layers.append( l3 )
    # Get the physical model (an array of rocks)    
    model = mb.channel(pad = args.pad,
                       thickness = args.thickness,
                       traces = args.ntraces,
                       layers = layers
                   )

    
    return modelr_plot( model, colourmap, args )
  

def main():
    parser = ArgumentParser(usage=short_description,
                            description=__doc__
                            )
                            
    parser.add_argument('time',
                        default=150,
                        type=int, 
                        help='The size in milliseconds of the plot'
                        )
                        
    args = parser.parse_args()
    run_script(args)
    
if __name__ == '__main__':
    main()
