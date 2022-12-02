import graphene

class SensorGQL(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    price = graphene.Int()
    description = graphene.String()
    
    manufacturer = graphene.Field(lambda: ManufacturerGQL)
    
    def resolve_manufacturer(parent, info):
        return parent.manufacturer

    category = graphene.Field(lambda: CategoryGQL)
    
    def resolve_category(parent, info):
        return parent.category
        
class ManufacturerGQL(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    
    sensors = graphene.List(lambda: SensorGQL)
    
    def resolve_sensors(parent, info):
        return parent.sensors

    categories = graphene.Field(graphene.List(lambda: CategoryGQL))
    
    def resolve_categories(parent, info):
        return parent.categories
    
class CategoryGQL(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()

    sensors = graphene.List(lambda: SensorGQL)
    
    def resolve_sensors(parent, info):
        return parent.sensors

    manufacturers = graphene.List(ManufacturerGQL)
    
    def resolve_manufacturers(parent, info):
        return parent.manufacturers