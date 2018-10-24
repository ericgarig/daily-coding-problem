"""
Daily Coding Problem.

Given a dictionary, print a 'high level' to 'low level' budget report.

E.g.:

Company - 10000000000
==================
Company - Accounting - 10000000
Company - Software - 100000
Company - Operations - 10000
===================
Company - Accounting - HR - 1000
Company - Accounting - Payroll - 100
Company - Software - Frontend - 100
Company - Software - Backend - 100
===================
Company - Accounting - HR - Frontend - 1
...
"""


def get_info():
    """Get department info."""
    return {
        "name": "Company",
        "budget": 10000000,
        "departments": [
            {
                "name": "Accounting",
                "budget": 10000,
                "departments": [
                    {
                        "name": "HR",
                        "budget": 100,
                        "departments": [
                            {
                                "name": "Metadata",
                                "budget": 1,
                            }
                        ]
                    },
                    {
                        "name": "Payroll",
                        "budget": 10000,
                        "departments": [
                            {
                                "name": "Payroll",
                                "budget": 1
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Software",
                "budget": 10000,
                "departments": [
                    {
                        "name": "Frontend",
                        "budget": 100,
                    },
                    {
                        "name": "Backend",
                        "budget": 100
                    }
                ]
            }
        ]
    }


def show_report(data):
    """Print out the report given the department info data."""
    if len(data) == 0:
        return True

    depts = []

    for i in data:
        try:
            parent = i['parent_name'] + ' - '
        except:
            parent = ''

        print parent + i['name'] + ' - ' + str(i['budget'])
        if 'departments' in i:
            # show_report(i['departments'], parent + i['name'])
            children = i['departments']
            for child in children:
                child['parent_name'] = parent + i['name']
            depts.extend(i['departments'])
            # print depts
    print '=================='
    show_report(depts)


show_report([get_info()])
