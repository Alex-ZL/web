from tastypie.resources import ModelResource

class ArecordResource(ModelResource):

	class Meta:
		list_allowed_methods = [ 'get', 'post' , 'delete']
		include_resource_uri = False
		resource_name = 'a_record'

	def post_record(self, request, **kwargs):
		deserialized = self.deserialize(request, request.raw_post_datas)
		kwargs = self.remove_api_resource_names(kwargs)
		owner_name = deserialized['OwnerName']
		record_data = deserialized['RecordData']
		text_representation = owner_name + ' IN A ' + record_data

		return text_representation
