**********************************************************
Make open data sharing a no-brainer for ethics committees.
**********************************************************

Statement of the problem
========================

The ideology of open and reproducible science makes its ways into
various fields of science.  Neuroimaging is a driving force today
behind many fields of brain sciences.  Despite possibly terabytes of
neuroimaging data collected for research daily, just a small fraction
becomes publicly available. Partially it is because management of
neuroimaging data requires to confirm to established legal norms,
i.e. addressing the aspect of subjects privacy.  Those norms are
usually established by institutional review boards (IRB, or otherwise
called ethics committees), which are in turn "governed" by the federal
regulations, such as `45 Code of Federal Regulations Part 46
<http://www.hhs.gov/ohrp/humansubjects/guidance/45cfr46.html>`_ in US.

Flexibility in interpretation of original regulations established in
the past century, decentralization of those committees, and lack of a
"community" influence over them created the problem: **for
neuroimaging studies there is no commonly accepted version of a
Consent form template which would allow for collected imaging data to
be shared as openly as possible while providing adequate guarantees
for subjects' privacy**.  In majority of the cases, used Consent forms
simply do not include **any** provision for public sharing of the data
to get a "speedy" IRB approval for a study.  Situation is particularly
tricky because major granting agencies (e.g. NIH, NSF) nowadays
require public data sharing, but do not provide explicit instructions
on *how*.

Overall approach
================

We would like to facilitate neuroimaging data sharing by any research
group by providing a "out of the box" solution address subjects
privacy:

- generally acceptable consent form allowing deposition of annonymized
  data to public data archives

- collection of tools/pipelines to help annonymisation of neuroimaging
  data making it ready for sharing


Consent form
------------

Goal minimum
~~~~~~~~~~~~

To address this problem we decided to collect :ref:`chap_consent_samples` which have
been previously approved by ethic committees in different
institutions.  Such samples could serve a basis for introducing
similar *ad-hoc* consent forms at other institutions so they fulfill
the desires of any particular committee, while allowing public sharing
of collected data.

Ultimate goal
~~~~~~~~~~~~~

Analysis of those might allow us to distill an
:ref:`chap_consent_ultimate` (or a set of those for different
use-cases and jurisdictions, and/or guidelines) which would be
compliant with all regulatory statues, while allowing for open sharing
and access to the neuroimaging data.

If regulated by the same federal/state laws, there is really no
objective reason why there could be no consensus among IRB committees
within the same jurisdiction. Although somewhat a utopian statement,
we hope that with examples/precedent cases and possibly **your**
enthusiastic involvement we cold achieve our goal.

Annonimization
--------------

Data must be de-identified before distribution.  We will collect
information on ref:`existing <annonimization_tools>`_ and possibly
establishing new pipelines to standardize annonimization of
neuroimaging data to simplify data sharing.


Useful links
============

- http://en.wikipedia.org/wiki/Institutional_review_board
- http://www.nsf.gov/bfa/dias/policy/hsfaqs.jsp

.. link list

`Bug tracker <https://github.com/neurodebian/open-brain-consent/issues>`_ |
`Build status <http://travis-ci.org/neurodebian/open-brain-consent>`_ |
`Documentation <https://open-brain-consent.readthedocs.org>`_
