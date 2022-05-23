**********************************************************
Make open data sharing a no-brainer for ethics committees.
**********************************************************

|Zenodo badge|

Statement of the problem
========================

The ideology of open and reproducible science makes its ways into various fields
of science.  Neuroimaging is a driving force today behind many fields of brain
sciences. Despite possibly terabytes of neuroimaging data collected for research
daily, just a small fraction becomes publicly available. Partially it is because
management of neuroimaging data requires to confirm to established legal norms,
i.e. addressing the aspect of research participants privacy.  Those norms are
usually established by institutional review boards (IRB, or otherwise called
ethics committees), which are in turn "governed" by national, federal and
supra-national regulations.

Flexibility in interpretation of original regulations established in
the past century, decentralization of those committees, and lack of a
"community" influence over them created the problem: **for
neuroimaging studies there was no commonly accepted version of a
Consent form template which would allow for collected imaging data to
be shared as openly as possible while providing adequate guarantees
for research participants' privacy**.  In majority of the cases, used Consent forms
simply did not include **any** provision for public sharing of the data
to get a "speedy" IRB approval for a study.  Situation is particularly
tricky because major granting agencies (e.g. NIH, NSF, RCUK) nowadays
require public data sharing, but do not provide explicit instructions
on *how*.

To facilitate neuroimaging data sharing, we providing an "out of
the box" solution addressing aforementioned human research participants
concerns and consisting of

- widely acceptable consent form templates (with various translations) allowing
  deposition of de-identified data to public data archives

- a template data user agreement (if your repository allows DUA instead of a licence)

- collection of tools/pipelines to help de-identification of neuroimaging
  data making it ready for sharing

You can read a summary of this work in our post-print: `The Open Brain Consent: Informing research participants and obtaining consent to share brain imaging data <https://psyarxiv.com/f6mnp/>`_

Sample Consent Forms
====================

To address this problem we collected :ref:`chap_consent_samples` which have
been previously approved by ethic committees in different
institutions.  Such samples can be used for
similar *ad-hoc* consent forms at other institutions so they fulfill
the desires of any particular committee, while allowing public sharing
of collected data.

Ultimate Consent Forms
======================

:ref:`chap_consent_ultimate` and :ref:`chap_gdpr_documents`
were created to provide suggested consent form(s) for different
use-cases, jurisdictions, and/or guidelines.

If regulated by the same supra-national/federal/state laws, there is really no
objective reason why there could be no consensus among IRB committees
within the same jurisdiction. Although somewhat a utopian statement,
we hope that with examples/precedent cases and possibly **your**
enthusiastic involvement we cold achieve our goal.

De-identification
=================

Data must be de-identified before distribution.  We will collect
information on :ref:`existing <chap_anonymization_tools>` and
possibly establishing an *ultimate* easy to use pipeline to
standardize de-identification of neuroimaging data to simplify data
sharing.

Useful links
============

- http://en.wikipedia.org/wiki/Institutional_review_board
- http://www.nsf.gov/bfa/dias/policy/hsfaqs.jsp

.. link list

`Issues <https://github.com/datalad/open-brain-consent/issues>`_ |
`Pull requests <https://github.com/datalad/open-brain-consent/pulls>`_ |
`Build status <http://travis-ci.org/datalad/open-brain-consent>`_ |
`Website <https://open-brain-consent.readthedocs.org>`_

.. |Zenodo badge| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.1411525.svg
   :target: https://doi.org/10.5281/zenodo.1411525
