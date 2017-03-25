.. _chap_anonymization_tools:

Anonymization tools
====================

Sanitization of headers/filenames
-----------------------------------

- see
  http://www.researchgate.net/post/Best_free_tool_for_DICOM_data_anonymization
  discussion on sanitization of DICOM headers
- `DeID <http://www.nitrc.org/projects/deid>`_ (`see paper 
  <http://journal.frontiersin.org/article/10.3389/fnins.2015.00325/full>`_),
  which provides an interactive tool for inspection and sanitization
  of Analyze and NIfTI images


Elimination of facial (and dental) features
-------------------------------------------

Skull stripping
~~~~~~~~~~~~~~~

One of the approaches is perform complete skull stripping, e.g. using

- `BET <http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/BET>`_ of `FSL
  <http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/>`_
- `3dSkullStrip
  <http://afni.nimh.nih.gov/pub/dist/doc/program_help/3dSkullStrip.html>`_
  of `AFNI <http://afni.nimh.nih.gov/>`_
-  `FreeSurfer <https://surfer.nmr.mgh.harvard.edu/>`_ 

Some dedicated anonymization tools work on this principle, e.g. `DeID`_

Faces/dental stripping
~~~~~~~~~~~~~~~~~~~~~~

More "gentle" approach is to strip out only the areas of face/mouth
leaving skull, which might be important for some types of analysis.
Usually achieved through alignment of pre-crafted mask to the subject
anatomy and removing of the masked out regions.

- `mri_deface <https://surfer.nmr.mgh.harvard.edu/fswiki/mri_deface>`_
  from `FreeSurfer <https://surfer.nmr.mgh.harvard.edu/>`_ (`paper from
  2007 with overview  <http://onlinelibrary.wiley.com/doi/10.1002/hbm.20312/full>`_)
- https://github.com/poldrack/openfmri/blob/master/pipeline/facemask/deface.py
- https://github.com/hanke/gumpdata/blob/master/scripts/conversion/convert_dicoms_anatomy#L26
- https://github.com/hanke/mridefacer

Rendering faces unrecognizable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Even more data/information preserving approach is to just obscure
facial features in the anatomical images:

- `Obscuring Surface Anatomy in Volumetric Imaging Data <http://link.springer.com/article/10.1007%2Fs12021-012-9160-3>`_
  Used for HCP data
- `QuickShear <https://github.com/nipy/quickshear/>`_ 

