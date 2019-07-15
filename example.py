
from gribby import GRIB
from gribby.section_0 import Section0
from gribby.section_1 import Section1
from gribby.section_11 import Section11


oc = {
    'centre': 54,
    'subcentre': 0,
    'local_tables_version_number': 0,
    'identification_of_project': 255,
    'production_status': 2,
    'originator_local_template_number': 255,
    'length_of_originator_local_template': 0
}

s0 = Section0(b'GRIB', b'  ', 0, 3, 12345)

s1 = Section1(**oc)

s11 = Section11(b'7777')

with open('jjj.grib3', 'wb') as fh:
    g = GRIB(fh)
    g.sections.append(s0)
    g.sections.append(s1)
    g.sections.append(s11)
    g.write()
