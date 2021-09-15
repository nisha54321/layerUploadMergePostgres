import os ,ogr
import psycopg2
import osgeo.ogr  

path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads/')

merge_directory = os.path.join(path, 'merge/')

if not os.path.exists(merge_directory):
   os.makedirs(merge_directory)
print("merge file ==================================")
def combine():
    print("merge file ==================================")
    fileEndsWith = '.gpkg'
    fileEndsWith1 = '.shp'
    outputMergefn = merge_directory+'mergefile.gpkg'
    fileList = os.listdir(UPLOAD_FOLDER)
    print(outputMergefn)
    #merge gpkg file
    first = True
    command = ''
    for file in fileList:
        if file.endswith(fileEndsWith) or file.endswith(fileEndsWith1):

            file1 = UPLOAD_FOLDER + file

            if first:
                command = 'ogr2ogr ' + outputMergefn + ' ' + file1+' -nln mergefile'
                first = False
            else:
                command = 'ogr2ogr -update -append ' + outputMergefn + ' '  + file1+' -nln mergefile' 

            os.system(command)

    #gpkg to postgresql

    connection1 = r"host=localhost port=5432 dbname=postgres user=postgres password=postgres"
    schema = "public"
    command = 'ogr2ogr -f "PostgreSQL" PG:"%s" -lco SCHEMA=%s "%s" -overwrite -progress -lco OVERWRITE=YES' % (connection1, schema, outputMergefn)

    os.system(command)
    print("upload postgres succss:================")

if __name__ == "__main__":
    combine()
