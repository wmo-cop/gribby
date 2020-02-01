
from gribby import GRIB
from gribby import sections

indicator_section = {
    'signature': b'GRIB',
    'reserved': b'  ',
    'master_tables_version_number': 0,
    'edition': 3
}

originator_section = {
    'centre': 54,
    'subcentre': 0,
    'local_tables_version_number': 0,
    'identification_of_project': 255,
    'production_status': 2,
    'originator_local_template_number': 255,
    'length_of_originator_local_template': 0
}

repetitions_and_index_section = {
    'total_number_of_repetitions': 1,
    'distinct_section3_greater_than_7_bytes': 1,
    'distinct_section4_greater_than_7_bytes': 1,
    'distinct_section5_greater_than_7_bytes': 1,
    'distinct_section6_greater_than_7_bytes': 1,
    'distinct_section7_greater_than_7_bytes': 1,
    'distinct_section8_greater_than_7_bytes': 1,
    'distinct_section9_greater_than_7_bytes': 1
}

time_domain_section = {
    'significance_of_reference_date_and_time': 3,
    'type_of_calendar': 0,
    'year': 2019,
    'month': 7,
    'day': 18,
    'hour': 14,
    'minute': 44,
    'second': 16,
    'time_domain_template_number': 65535,
}

horizontal_domain_section = {
    'number_of_points_in_domain': 5,
    'horizontal_domain_template_number': 0,
}
# Thu Jul 18 14:44:16 GMT 2019

#s0 = sections.Section0(b'GRIB', b'  ', 0, 3, 12345)

s0 = sections.Section0(**indicator_section)
s1 = sections.Section1(**originator_section)
s2 = sections.Section2(**repetitions_and_index_section)
s3 = sections.Section3(**time_domain_section)
s11 = sections.Section11(b'7777')

with open('jjj.grib3', 'wb') as fh:
    g = GRIB(fh)
    g.sections.append(s0)
    g.sections.append(s1)
    g.sections.append(s2)
    g.sections.append(s3)
    g.sections.append(s11)
    g.write()
