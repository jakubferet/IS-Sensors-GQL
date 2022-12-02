import graphene
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from queries import QueryGQL
from mutations import Mutations
from connection import defineStartupAndShutdown, SessionMaker


graphql_app = GraphQLApp(
    schema=graphene.Schema(query=QueryGQL, mutation=Mutations),
    on_get=make_graphiql_handler())

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_route('/gql/', graphql_app)

'''
@app.get("/{id}")
def readSensor(id):
    sensor = QueryGQL.resolve_sensor(QueryGQL,"info",id)
    return sensor.name
'''

defineStartupAndShutdown(app, SessionMaker)