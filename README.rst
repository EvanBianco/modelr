Welcome to modelr's documentation!
==================================

Google charts like API for geophysics! Submit tasks via a script-plus-parameters, or via a URL. 

Example: 

* `<http://server.modelr.org:8080/plot.jpeg?script=one_spike.py&title=Ricker&f=25&reflectivity_model=zoeppritz&Rpp0=2350,2350,1200&Rpp1=2670,2560,1300&theta1=45>`_

Or to get help just run:

* `<http://server.modelr.org:8080/plot.jpeg>`_

Prerequisites
++++++++++++++++
.. line-block::
   You will need scientific python (numpy, scipy, matplotlib), which come with
   Enthought Canopy:  `<http://www.enthought.com>`_

   They can alternatively be installed via pip, aptitude, ports,
   or sourced from git.

   Additionally, ImageMagick will need to be installed in order to
   handle conversion of svg to png. 
   Binaries can be downloaded from the ImageMagick website: 
   `<http://www.imagemagick.org/script/binary-releases.php#unix>`_

   ImageMagick can also be installed via ports or aptitude.

   Other python packages that will be automatically installed during setup:

* agilegeo
* pypng
* requests
* jinja2
* svgwrite






Links
+++++++++++

* `Agile Geoscience <http://www.agilegeoscience.com>`_
* `Homepage <http://agile-geoscience.github.com/modelr/>`_
* `Issue Tracker <https://github.com/agile-geoscience/modelr/issues/>`_


* `PyPi <http://pypi.python.org/pypi/modelr/>`_
* `Github <https://github.com/agile-geoscience/modelr>`_


Authors
++++++++++++++++

* `Matt Hall <https://github.com/kwinkunks>`_ @ `Agile Geoscience <http://www.agilegeoscience.com>`_
* `Sean Ross-Ross <https://github.com/srossross>`_ @ now at `Continuum`
* `Evan Bianco <https://github.com/EvanBianco>`_ @ `Agile Geoscience <http://www.agilegeoscience.com>`_
* `Ben Bougher <https://github.com/ben-bougher>`_

