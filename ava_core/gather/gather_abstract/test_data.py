# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.gather.gather_abstract.models import GatherHistory


# Implementation
class GatherHistoryTestData(AvaCoreTestData):
    """
    Test data for GatherHistory
    """

    @staticmethod
    def init_requirements(owner):
        # Import the required model and data
        from ava_core.gather.gather_office365.models import Office365GatherHistory
        from ava_core.gather.gather_office365.test_data import Office365GatherHistoryTestData
        # Grab data for object creation, with owner if required.
        data_model = Office365GatherHistoryTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Office365GatherHistory.objects.filter(owner=owner['email']) if 'email' in standard_data else Office365GatherHistory.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            Office365GatherHistoryTestData.init_requirements(owner)
            model = Office365GatherHistory.objects.create(**standard_data)
            model = Office365GatherHistory.objects.create(**unique_data)

        # Import the required model and data
        from ava_core.gather.gather_google.models import GoogleGatherHistory
        from ava_core.gather.gather_google.test_data import GoogleGatherHistoryTestData
        # Grab data for object creation, with owner if required.
        data_model = GoogleGatherHistoryTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = GoogleGatherHistory.objects.filter(owner=owner['email']) if 'email' in standard_data else GoogleGatherHistory.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            GoogleGatherHistoryTestData.init_requirements(owner)
            model = GoogleGatherHistory.objects.create(**standard_data)
            model = GoogleGatherHistory.objects.create(**unique_data)

        # Import the required model and data
        from ava_core.gather.gather_ldap.models import LDAPGatherHistory
        from ava_core.gather.gather_ldap.test_data import LDAPGatherHistoryTestData
        # Grab data for object creation, with owner if required.
        data_model = LDAPGatherHistoryTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = LDAPGatherHistory.objects.filter(owner=owner['email']) if 'email' in standard_data else LDAPGatherHistory.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            LDAPGatherHistoryTestData.init_requirements(owner)
            model = LDAPGatherHistory.objects.create(**standard_data)
            model = LDAPGatherHistory.objects.create(**unique_data)

    # Store self information
    model = GatherHistory
    url = 'example/'

    standard = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }

    unique = {
        'no_people': 54321,
        'office365gatherhistory': 'default',
        'message': 'unique_char',
        'no_groups': 54321,
        'no_identifiers': 54321,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 1,
    }

    missing_no_people = {
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }
    modified_no_people = {
        'no_people': 54321,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }

    missing_office365gatherhistory = {
        'no_people': 12345,
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }
    modified_office365gatherhistory = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }

    missing_message = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }
    modified_message = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'modified_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }

    modified_no_groups = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 54321,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }
    missing_no_groups = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }

    modified_no_identifiers = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 54321,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }
    missing_no_identifiers = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }

    missing_googlegatherhistory = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }
    modified_googlegatherhistory = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }

    missing_next_scheduled = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }
    modified_next_scheduled = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }

    missing_ldapgatherhistory = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'import_status': 0,
    }
    modified_ldapgatherhistory = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }

    missing_import_status = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
    }
    modified_import_status = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 1,
    }




