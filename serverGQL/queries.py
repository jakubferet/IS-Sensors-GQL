import graphene

from gql_models import SensorGQL, ManufacturerGQL, CategoryGQL
from sql_models import SensorModel, ManufacturerModel, CategoryModel
from connection import extractSession


class QueryGQL(graphene.ObjectType):
    sensor = graphene.Field(SensorGQL, id = graphene.ID(required = True))
    manufacturer = graphene.Field(ManufacturerGQL, id = graphene.ID(required = True))
    category = graphene.Field(CategoryGQL, id = graphene.ID(required = True))
    sensors = graphene.List(SensorGQL)
    manufacturers = graphene.List(ManufacturerGQL)
    categories = graphene.List(CategoryGQL)
    
    def resolve_sensor(root, info, id):
        session = extractSession(info)
        result = session.query(SensorModel).filter(SensorModel.id==id).first()
        return result
    
    def resolve_manufacturer(root, info, id):
        session = extractSession(info)
        result = session.query(ManufacturerModel).filter(ManufacturerModel.id==id).first()
        return result    
    
    def resolve_category(root, info, id):
        session = extractSession(info)
        result = session.query(CategoryModel).filter(CategoryModel.id==id).first()
        return result

    def resolve_sensors(root, info):
        session = extractSession(info)
        result = session.query(SensorModel)
        return result
    
    def resolve_manufacturers(root, info):
        session = extractSession(info)
        result = session.query(ManufacturerModel)
        return result    
    
    def resolve_categories(root, info):
        session = extractSession(info)
        result = session.query(CategoryModel)
        return result