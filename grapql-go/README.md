Go is a modern general purpose programming language designed by google; best known for it’s simplicity, concurrency and fast performance.

gqlgen is a library for creating GraphQL applications in Go.

API will be able to handle registration, authentication, submitting links and getting list of links.

Here is a description from gqlgen about the generated files:
- gqlgen.yml — The gqlgen config file, knobs for controlling the generated code.
- graph/generated/generated.go — The GraphQL execution runtime, the bulk of the generated code.
- graph/model/models_gen.go — Generated models required to build the graph. Often you will override these with your own models. Still very useful for input types.
- graph/schema.graphqls — This is the file where you will add GraphQL schemas.
- graph/schema.resolvers.go — This is where your application code lives. generated.go will call into this to get the data the user has requested.
- server.go — This is a minimal entry point that sets up an http.Handler to the generated GraphQL server. start the server with go run server.go and open your browser and you should see 
