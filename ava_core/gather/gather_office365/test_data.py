# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.gather.gather_office365.models import Office365GatherHistory


# Implementation
class Office365GatherHistoryTestData(AvaCoreTestData):
    """
    Test data for Office365GatherHistory
    """

    @staticmethod
    def init_requirements(owner):
        # Import the required model and data
        from ava_core.gather.gather_abstract.models import GatherHistory
        from ava_core.gather.gather_abstract.test_data import GatherHistoryTestData
        # Grab data for object creation, with owner if required.
        data_model = GatherHistoryTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = GatherHistory.objects.filter(owner=owner['email']) if 'email' in standard_data else GatherHistory.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            GatherHistoryTestData.init_requirements(owner)
            model = GatherHistory.objects.create(**standard_data)
            model = GatherHistory.objects.create(**unique_data)

        # Import the required model and data
        from ava_core.integration.integration_office365.models import Office365IntegrationAdapter
        from ava_core.integration.integration_office365.test_data import Office365IntegrationAdapterTestData
        # Grab data for object creation, with owner if required.
        data_model = Office365IntegrationAdapterTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Office365IntegrationAdapter.objects.filter(owner=owner['email']) if 'email' in standard_data else Office365IntegrationAdapter.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            Office365IntegrationAdapterTestData.init_requirements(owner)
            model = Office365IntegrationAdapter.objects.create(**standard_data)
            model = Office365IntegrationAdapter.objects.create(**unique_data)

    # Store self information
    model = Office365GatherHistory
    url = 'example/'

    standard = {
        'gatherhistory_ptr': 'default',
        'integration': 'example//1/',
    }

    unique = {
        'gatherhistory_ptr': 'default',
        'integration': 'example//2/',
    }

    modified_gatherhistory_ptr = {
        'gatherhistory_ptr': 'default',
        'integration': 'example//1/',
    }
    missing_gatherhistory_ptr = {
        'integration': 'example//1/',
    }

    missing_integration = {
        'gatherhistory_ptr': 'default',
    }
    modified_integration = {
        'gatherhistory_ptr': 'default',
        'integration': 'example//2/',
    }



