from moto import mock_s3
import unittest
import boto3
from s3_operations import list_s3_buckets, get_s3_client, list_s3_objects, read_s3_object


class S3TestCase(unittest.TestCase):
    def setUp(self):
        self.bucket ='dakobed-transcriptions'
        self.key = 'mddarr/blues.wav'
        self.value = 'value'

    @mock_s3
    def __moto_setup(self):
        """
        Simulate s3 file upload
        """
        s3 = get_s3_client()
        s3.create_bucket(Bucket=self.bucket)
        s3.put_object(Bucket=self.bucket, Key = self.key, Body= self.value)

    @mock_s3
    def test_get_client(self):
        s3=get_s3_client()
        self.assertEqual(s3._endpoint.host, 'https://s3.us-west-2.amazonaws.com')

    @mock_s3
    def test_list_s3_objects(self):
        self.__moto_setup()
        objects = [object for object in list_s3_objects(self.bucket)]
        self.assertTrue(self.key in objects)
    #
    @mock_s3
    def test_read_s3_object(self):
        self.__moto_setup()
        self.__moto_setup()
        content = read_s3_object(self.bucket, self.key)
        self.assertEqual(content.decode('utf-8'), 'value')


if __name__ == '__main__':
    unittest.main()