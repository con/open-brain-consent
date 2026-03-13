.. _chap_duo:

DUO (Data Use Ontology) Annotation
===================================

The `Data Use Ontology (DUO) <https://github.com/EBISPOT/DUO>`_ provides standardized codes to describe data use conditions and permissions.
Annotating datasets with DUO codes helps automated systems match data access requests to the conditions under which data were consented for sharing.

Below we provide a mapping of OBC consent form versions to DUO codes.
This can be used when annotating datasets (e.g., in BIDS ``dataset_description.json``) to indicate the data use conditions established by the consent form used during data collection.

.. note::

   DUO currently lacks a code for **"no re-identification"** — a condition central to all OBC forms and the :ref:`Data User Agreement <chap_dua>`.
   This gap has been raised in `EBISPOT/DUO#129 <https://github.com/EBISPOT/DUO/issues/129>`_.


OBC-ULT — Single access type (all data shared publicly)
--------------------------------------------------------

- **DUO:0000042** — General Research Use (GRU): use is allowed for general research use for any research purpose.

The form states that future projects "can focus on any topic that might be unrelated to the goals of this study" and data are shared with "the general public via the Internet and a fully open database."


OBC-ULT-2T — Two access types
------------------------------

**Public tier:**

- **DUO:0000042** — General Research Use (GRU)

**Controlled access tier:**

- **DUO:0000042** — General Research Use (GRU)
- **DUO:0000026** — User Specific Restriction (US): use is limited to approved users. The form states that "a committee of experts will carefully review every data request from other scientists before allowing them to use this controlled access database."


OBC-GDPR-ULT — GDPR edition
----------------------------

- **DUO:0000006** — Health or Medical or Biomedical Research (HMB): use is allowed for health, medical, or biomedical purposes.

The form restricts future use to "research projects in the field of medical and cognitive neuroscience," which falls within the scope of HMB.

GDPR requirements (data protection, transfer outside EU, withdrawal rights) operate at the regulatory/policy level and are not represented as DUO codes.
The :ref:`Data User Agreement <chap_dua>` further constrains data use (no re-identification, no redistribution, attribution) but these conditions do not yet have DUO equivalents.
