# PyQus

Python codes for post-processing of Abaqus ODB files.

![](pyqus/docs/source/_static/pyqus_logo.png)

### Project status

Developing **(0.1.0-dev)**

### Capabilities

* Read basic properties from ODB file
  - Parts
  - Instances
  - Materials properties
  - Steps
  - Analysis type
* Get elements connectivity.
* Get nodes coordinates.
* Calculate distance between two nodes.
* Get maximum value (all instances, all steps)
  - Max. von Mises Stresses
  - Max. Plastic Equivalent Strains
  - Max. Nominal Strains
  - Max. Reaction forces
  - Max. Velocity (Magnitude)
* Get nodal position in time

### Modules

* **iodb**: For IO odb files.
* **graph**: For plots with maplotlib library.
* **report**: For write HTML and PDF(LaTeX) report.
* **abq**: For preprocessing operations. (Geometry, Materials, Sections,...)

### More info...

```
Developer: Pedro Jorge De Los Santos
E-mail: delossantosmfq@gmail.com
Blog: labdls.blogspot.mx
License: MIT License (See LICENSE)
```

