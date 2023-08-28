SET HERMIT_FILES_ROOT=D:\projects\projects\hermit\api\files
call uvicorn index:api --port 8080 --host localhost --reload
exit