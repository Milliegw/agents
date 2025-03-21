 MSYS_NO_PATHCONV=1 docker run --rm -it \
-v "$PWD":/usr/local/structurizr \
structurizr/cli \
validate -w test.dsl
