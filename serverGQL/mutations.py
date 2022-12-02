import graphene

from gql_models import SensorGQL, ManufacturerGQL, CategoryGQL
from sql_models import SensorModel, ManufacturerModel, CategoryModel
from connection import extractSession

###   SENSOR  ###

class SensorInput(graphene.InputObjectType):
    id = graphene.ID(required=False)
    name = graphene.String(required=False)
    price = graphene.Int(required=False)
    description = graphene.String(required=False)
    manufacturer_id = graphene.ID(required=False)
    category_id = graphene.ID(required=False)
    
class CreateSensorGQL(graphene.Mutation):
    class Arguments:
        sensor_input = SensorInput(required = True)
    
    ok = graphene.Boolean()
    result = graphene.Field(SensorGQL)
    
    def mutate(parent, info, sensor_input):
        session = extractSession(info)
        sensor = SensorModel(
            id = sensor_input.id,
            name = sensor_input.name,
            price = sensor_input.price,
            description = sensor_input.description,
            manufacturer_id = sensor_input.manufacturer_id,
            category_id = sensor_input.category_id
        )
        session.add(sensor)
        session.commit()
        session.refresh(sensor)
        return CreateSensorGQL(ok=True, result=sensor)
    
class UpdateSensorGQL(graphene.Mutation):
    class Arguments:
        sensor_input = SensorInput(required = True)
    
    ok = graphene.Boolean()
    result = graphene.Field(SensorGQL)
    
    def mutate(parent, info, sensor_input):
        session = extractSession(info)
        
        sensor = session.query(SensorModel).filter(SensorModel.id==sensor_input.id).first()
        if sensor_input.name != None:
            sensor.name = sensor_input.name
        if sensor_input.price != None:
            sensor.price = sensor_input.price
        if sensor_input.description != None:
            sensor.description = sensor_input.description
        if sensor_input.manufacturer_id != None:
            sensor.manufacturer_id = sensor_input.manufacturer_id
        if sensor_input.category_id != None:
            sensor.category_id = sensor_input.category_id

        session.commit()     
        session.refresh(sensor)
        return UpdateSensorGQL(ok=True, result=sensor)

class DeleteSensorGQL(graphene.Mutation):
    class Arguments:
        sensor_input = SensorInput(required = True)

    ok = graphene.Boolean()
    result = graphene.Field(SensorGQL)

    def mutate(parent, info, sensor_input):
        session = extractSession(info)
        sensor = session.query(SensorModel).filter(SensorModel.id==sensor_input.id).first()
        session.delete(sensor)
        session.commit()     
        return DeleteSensorGQL(ok=True, result=sensor)

###   MANUFACTURER  ###

class ManufacturerInput(graphene.InputObjectType):
    id = graphene.ID(required=False)
    name = graphene.String(required=False)
    description = graphene.String(required=False)
    category_id = graphene.ID(required=False)
    
class CreateManufacturerGQL(graphene.Mutation):
    class Arguments:
        manufacturer_input = ManufacturerInput(required = True)
    
    ok = graphene.Boolean()
    result = graphene.Field(ManufacturerGQL)
    
    def mutate(parent, info, manufacturer_input):
        session = extractSession(info)
        manufacturer = ManufacturerModel(
            id = manufacturer_input.id,
            name = manufacturer_input.name,
            description = manufacturer_input.description
        )
        category = session.query(CategoryModel).filter(CategoryModel.id==manufacturer_input.category_id).first()
        if category != None:
            manufacturer.categories.append(category)

        session.add(manufacturer)
        session.commit()
        session.refresh(manufacturer)
        return CreateManufacturerGQL(ok=True, result=manufacturer)
    
class UpdateManufacturerGQL(graphene.Mutation):
    class Arguments:
        manufacturer_input = ManufacturerInput(required = True)
    
    ok = graphene.Boolean()
    result = graphene.Field(ManufacturerGQL)
    
    def mutate(parent, info, manufacturer_input):
        session = extractSession(info)

        manufacturer = session.query(ManufacturerModel).filter(ManufacturerModel.id==manufacturer_input.id).first()
        if manufacturer_input.name != None:
            manufacturer.name = manufacturer_input.name
        if manufacturer_input.description != None:
            manufacturer.description = manufacturer_input.description

        category = session.query(CategoryModel).filter(CategoryModel.id==manufacturer_input.category_id).first()
        if category != None:
            manufacturer.categories.append(category)

        session.commit()     
        session.refresh(manufacturer)
        return UpdateManufacturerGQL(ok=True, result=manufacturer)

class DeleteManufacturerGQL(graphene.Mutation):
    class Arguments:
        manufacturer_input = ManufacturerInput(required = True)

    ok = graphene.Boolean()
    result = graphene.Field(ManufacturerGQL)

    def mutate(parent, info, manufacturer_input):
        session = extractSession(info)
        manufacturer = session.query(ManufacturerModel).filter(ManufacturerModel.id==manufacturer_input.id).first()
        session.delete(manufacturer)
        session.commit()     
        return DeleteManufacturerGQL(ok=True, result=manufacturer)

###   CATEGORY  ###

class CategoryInput(graphene.InputObjectType):
    id = graphene.ID(required=False)
    name = graphene.String(required=False)
    manufacturer_id = graphene.ID(required=False)
    
class CreateCategoryGQL(graphene.Mutation):
    class Arguments:
        category_input = CategoryInput(required = True)
    
    ok = graphene.Boolean()
    result = graphene.Field(CategoryGQL)
    
    def mutate(parent, info, category_input):
        session = extractSession(info)
        category = CategoryModel(
            id = category_input.id,
            name = category_input.name
        )
        manufacturer = session.query(ManufacturerModel).filter(ManufacturerModel.id==category_input.manufacturer_id).first()
        if manufacturer != None:
            category.manufacturers.append(manufacturer)

        session.add(category)
        session.commit()
        session.refresh(category)
        return CreateCategoryGQL(ok=True, result=category)
    
class UpdateCategoryGQL(graphene.Mutation):
    class Arguments:
        category_input = CategoryInput(required = True)
    
    ok = graphene.Boolean()
    result = graphene.Field(CategoryGQL)
    
    def mutate(parent, info, category_input):
        session = extractSession(info)

        category = session.query(CategoryModel).filter(CategoryModel.id==category_input.id).first()
        if category_input.name != None:
            category.name = category_input.name

        manufacturer = session.query(ManufacturerModel).filter(ManufacturerModel.id==category_input.manufacturer_id).first()
        if manufacturer != None:
            category.manufacturers.append(manufacturer)

        session.commit()     
        session.refresh(category)
        return UpdateCategoryGQL(ok=True, result=category)

class DeleteCategoryGQL(graphene.Mutation):
    class Arguments:
        category_input = CategoryInput(required = True)

    ok = graphene.Boolean()
    result = graphene.Field(CategoryGQL)

    def mutate(parent, info, category_input):
        session = extractSession(info)
        category = session.query(CategoryModel).filter(CategoryModel.id==category_input.id).first()
        session.delete(category)
        session.commit()     
        return DeleteCategoryGQL(ok=True, result=category)

###   MUTATIONS CLASS   ###

class Mutations(graphene.ObjectType):
    create_sensor = CreateSensorGQL.Field()
    update_sensor = UpdateSensorGQL.Field()
    delete_sensor = DeleteSensorGQL.Field()
    
    create_manufacturer = CreateManufacturerGQL.Field()
    update_manufacturer = UpdateManufacturerGQL.Field()
    delete_manufacturer = DeleteManufacturerGQL.Field()
    
    create_category = CreateCategoryGQL.Field()
    update_category = UpdateCategoryGQL.Field()
    delete_category = DeleteCategoryGQL.Field()