# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test import AvaCoreTest
from ava_core.report.test_data import ReportResponseTestData, SuspiciousTestData, QuestionTestData


# Implementation
class ReportResponseTest(AvaCoreTest):
    """
    ReportResponse Test
    """

    def setUp(self):
        # Make call to super.
        super(ReportResponseTest, self).setUp()

        # Set the data type.
        self.data = ReportResponseTestData
        self.data.init_requirements()

    def test_report_response_create_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data('standard')

        # Make post request and ensure created response.
        response = self.client.post(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_report_response_create_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data('standard')

        # Make post request and ensure created response.
        response = self.client.post(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_report_response_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data('standard')

        # Make post request and ensure unauthorized response.
        response = self.client.post(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_report_response_retrieve_single_as_user(self):
        # Create new ReportResponse models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))

    def test_report_response_retrieve_all_as_user(self):
        # Create new ReportResponse models.
        self.create_model_logout(self.data, data_name='standard', owner=self.user_user)
        self.create_model_logout(self.data, data_name='modified', owner=self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))

    def test_report_response_retrieve_single_as_admin(self):
        # Create new ReportResponse models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))

    def test_report_response_retrieve_all_as_admin(self):
        # Create new ReportResponse models.
        self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        self.create_model_logout(self.data, data_name='modified', owner=self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))

    def test_report_response_retrieve_single_as_unauthorized(self):
        # Create new ReportResponse models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)

    def test_report_response_retrieve_all_as_unauthorized(self):
        # Create new ReportResponse models.
        self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        self.create_model_logout(self.data, data_name='modified', owner=self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)

    # TODO:    Write retrieve owner tests    def test_report_response_update_exists_as_user(self):
        # Create new ReportResponse models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_user)
        # Log in as user.
        self.login_user(self.user_user)

        # Make put request and ensure OK response.
        response = self.client.put(url, self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_url(url, self.data.unique))

    def test_report_response_update_does_not_exist_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Make put request and ensure not found response.
        response = self.client.put(self.format_url(self.data.url + '/9999'), self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_report_response_update_exists_as_admin(self):
        # Create new ReportResponse models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make put request and ensure OK response.
        response = self.client.put(url, self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_url(url, self.data.unique))

    def test_report_response_update_does_not_exist_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make put request and ensure not found response.
        response = self.client.put(self.format_url(self.data.url + '/9999'), self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_report_response_update_exists_as_unauthorized(self):
        # Create new ReportResponse models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Make put request and ensure unauthorized response.
        response = self.client.put(url, self.data.get_data('unique'))
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertTrue(self.does_contain_data_url(url, self.data.standard))

    def test_report_response_update_does_not_exist_as_unauthorized(self):
        # Make put request and ensure unauthorized response.
        response = self.client.put(self.format_url(self.data.url + '/9999'), self.data.get_data('unique'))
        self.assertIn(response.status_code, self.status_forbidden)

    # TODO:    Write update owner tests    def test_report_response_delete_exists_as_user(self):
        # Create new ReportResponse models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_user)
        # Log in as user.
        self.login_user(self.user_user)

        # Make delete request and ensure no content response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.data.model.objects.count(), 0)

    def test_report_response_delete_does_not_exist_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Make delete request and ensure not found response
        response = self.client.get(self.format_url(self.data.url + '/9999'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_report_response_delete_exists_as_admin(self):
        # Create new ReportResponse models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make delete request and ensure no content response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.data.model.objects.count(), 0)

    def test_report_response_delete_does_not_exist_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make delete request and ensure not found response
        response = self.client.get(self.format_url(self.data.url + '/9999'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_report_response_delete_exists_as_unauthorized(self):
        # Create new ReportResponse models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Make delete request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), 1)

    def test_report_response_delete_does_not_exist_as_unauthorized(self):
        # Make delete request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url + '/9999'))
        self.assertIn(response.status_code, self.status_forbidden)

    # TODO:    Write delete owner tests
class SuspiciousTest(AvaCoreTest):
    """
    Suspicious Test
    """

    def setUp(self):
        # Make call to super.
        super(SuspiciousTest, self).setUp()

        # Set the data type.
        self.data = SuspiciousTestData
        self.data.init_requirements()

    def test_suspicious_create_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data('standard')

        # Make post request and ensure created response.
        response = self.client.post(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_suspicious_create_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data('standard')

        # Make post request and ensure created response.
        response = self.client.post(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_suspicious_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data('standard')

        # Make post request and ensure unauthorized response.
        response = self.client.post(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_suspicious_retrieve_single_as_user(self):
        # Create new Suspicious models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))

    def test_suspicious_retrieve_all_as_user(self):
        # Create new Suspicious models.
        self.create_model_logout(self.data, data_name='standard', owner=self.user_user)
        self.create_model_logout(self.data, data_name='modified', owner=self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))

    def test_suspicious_retrieve_single_as_admin(self):
        # Create new Suspicious models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))

    def test_suspicious_retrieve_all_as_admin(self):
        # Create new Suspicious models.
        self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        self.create_model_logout(self.data, data_name='modified', owner=self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))

    def test_suspicious_retrieve_single_as_unauthorized(self):
        # Create new Suspicious models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)

    def test_suspicious_retrieve_all_as_unauthorized(self):
        # Create new Suspicious models.
        self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        self.create_model_logout(self.data, data_name='modified', owner=self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)

    # TODO:    Write retrieve owner tests    def test_suspicious_update_exists_as_user(self):
        # Create new Suspicious models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_user)
        # Log in as user.
        self.login_user(self.user_user)

        # Make put request and ensure OK response.
        response = self.client.put(url, self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_url(url, self.data.unique))

    def test_suspicious_update_does_not_exist_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Make put request and ensure not found response.
        response = self.client.put(self.format_url(self.data.url + '/9999'), self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_suspicious_update_exists_as_admin(self):
        # Create new Suspicious models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make put request and ensure OK response.
        response = self.client.put(url, self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_url(url, self.data.unique))

    def test_suspicious_update_does_not_exist_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make put request and ensure not found response.
        response = self.client.put(self.format_url(self.data.url + '/9999'), self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_suspicious_update_exists_as_unauthorized(self):
        # Create new Suspicious models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Make put request and ensure unauthorized response.
        response = self.client.put(url, self.data.get_data('unique'))
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertTrue(self.does_contain_data_url(url, self.data.standard))

    def test_suspicious_update_does_not_exist_as_unauthorized(self):
        # Make put request and ensure unauthorized response.
        response = self.client.put(self.format_url(self.data.url + '/9999'), self.data.get_data('unique'))
        self.assertIn(response.status_code, self.status_forbidden)

    # TODO:    Write update owner tests    def test_suspicious_delete_exists_as_user(self):
        # Create new Suspicious models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_user)
        # Log in as user.
        self.login_user(self.user_user)

        # Make delete request and ensure no content response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.data.model.objects.count(), 0)

    def test_suspicious_delete_does_not_exist_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Make delete request and ensure not found response
        response = self.client.get(self.format_url(self.data.url + '/9999'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_suspicious_delete_exists_as_admin(self):
        # Create new Suspicious models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make delete request and ensure no content response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.data.model.objects.count(), 0)

    def test_suspicious_delete_does_not_exist_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make delete request and ensure not found response
        response = self.client.get(self.format_url(self.data.url + '/9999'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_suspicious_delete_exists_as_unauthorized(self):
        # Create new Suspicious models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Make delete request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), 1)

    def test_suspicious_delete_does_not_exist_as_unauthorized(self):
        # Make delete request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url + '/9999'))
        self.assertIn(response.status_code, self.status_forbidden)

    # TODO:    Write delete owner tests
class QuestionTest(AvaCoreTest):
    """
    Question Test
    """

    def setUp(self):
        # Make call to super.
        super(QuestionTest, self).setUp()

        # Set the data type.
        self.data = QuestionTestData
        self.data.init_requirements()

    def test_question_create_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data('standard')

        # Make post request and ensure created response.
        response = self.client.post(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_question_create_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data('standard')

        # Make post request and ensure created response.
        response = self.client.post(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_question_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data('standard')

        # Make post request and ensure unauthorized response.
        response = self.client.post(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_question_retrieve_single_as_user(self):
        # Create new Question models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))

    def test_question_retrieve_all_as_user(self):
        # Create new Question models.
        self.create_model_logout(self.data, data_name='standard', owner=self.user_user)
        self.create_model_logout(self.data, data_name='modified', owner=self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))

    def test_question_retrieve_single_as_admin(self):
        # Create new Question models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))

    def test_question_retrieve_all_as_admin(self):
        # Create new Question models.
        self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        self.create_model_logout(self.data, data_name='modified', owner=self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))

    def test_question_retrieve_single_as_unauthorized(self):
        # Create new Question models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)

    def test_question_retrieve_all_as_unauthorized(self):
        # Create new Question models.
        self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        self.create_model_logout(self.data, data_name='modified', owner=self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)

    # TODO:    Write retrieve owner tests    def test_question_update_exists_as_user(self):
        # Create new Question models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_user)
        # Log in as user.
        self.login_user(self.user_user)

        # Make put request and ensure OK response.
        response = self.client.put(url, self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_url(url, self.data.unique))

    def test_question_update_does_not_exist_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Make put request and ensure not found response.
        response = self.client.put(self.format_url(self.data.url + '/9999'), self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_question_update_exists_as_admin(self):
        # Create new Question models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make put request and ensure OK response.
        response = self.client.put(url, self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_url(url, self.data.unique))

    def test_question_update_does_not_exist_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make put request and ensure not found response.
        response = self.client.put(self.format_url(self.data.url + '/9999'), self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_question_update_exists_as_unauthorized(self):
        # Create new Question models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Make put request and ensure unauthorized response.
        response = self.client.put(url, self.data.get_data('unique'))
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertTrue(self.does_contain_data_url(url, self.data.standard))

    def test_question_update_does_not_exist_as_unauthorized(self):
        # Make put request and ensure unauthorized response.
        response = self.client.put(self.format_url(self.data.url + '/9999'), self.data.get_data('unique'))
        self.assertIn(response.status_code, self.status_forbidden)

    # TODO:    Write update owner tests    def test_question_delete_exists_as_user(self):
        # Create new Question models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_user)
        # Log in as user.
        self.login_user(self.user_user)

        # Make delete request and ensure no content response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.data.model.objects.count(), 0)

    def test_question_delete_does_not_exist_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Make delete request and ensure not found response
        response = self.client.get(self.format_url(self.data.url + '/9999'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_question_delete_exists_as_admin(self):
        # Create new Question models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make delete request and ensure no content response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.data.model.objects.count(), 0)

    def test_question_delete_does_not_exist_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make delete request and ensure not found response
        response = self.client.get(self.format_url(self.data.url + '/9999'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_question_delete_exists_as_unauthorized(self):
        # Create new Question models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Make delete request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), 1)

    def test_question_delete_does_not_exist_as_unauthorized(self):
        # Make delete request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url + '/9999'))
        self.assertIn(response.status_code, self.status_forbidden)

    # TODO:    Write delete owner tests

