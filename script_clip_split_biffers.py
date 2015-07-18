import arcpy
from arcpy import env
import os, numpy

arcpy.env.workspace=r"E:\data_2015\Mitra\Pasta_mapeamentos_completo_2015_07_d13"
lista_mapas=arcpy.ListFeatureClasses()



arcpy.env.workspace=r"E:\data_2015\Mitra\Buffers_frags_frags_correto_revisado"
lista_buffers=arcpy.ListFeatureClasses()



#---------------------------------------------------------------------------------------------------------------------------------------------
# clipando o mapa a partir de cada buffer
arcpy.env.workspace=r"E:\data_2015\Mitra\Pasta_mapeamentos_completo_2015_07_d13\Clip_split_0125"
for i in lista_mapas:
    inpname=i.replace(".shp","")
    pattern=i[30:34]
    print pattern
    for a in lista_buffers:
        
        if pattern in a:
            fc=a.replace(".shp","")
            print fc ,"**", inpname
            fields="FID"
            with arcpy.da.SearchCursor(fc, fields) as cursor:
                for row in cursor:
                    x=0
                    format="0000"+`row[0]`
                    format=format[-2:]
                    outpuname=inpname+"_FID_"+format
                    query="FID=%d"%row[0]
                    arcpy.SelectLayerByAttribute_management(fc,"NEW_SELECTION",query)
                    
                    arcpy.Clip_analysis(inpname,fc,outpuname,"")
                    arcpy.SelectLayerByAttribute_management(fc,"CLEAR_SELECTION") 
                #print fc ,"**", inpname
                arcpy.SelectLayerByAttribute_management(fc,"CLEAR_SELECTION") 
#---------------------------------------------------------------------------------------------------------------------------------------------                    
                   




#---------------------------------------------------------------------------------------------------------------------------------------------
# 125   calculando a PCT para a escala de 0125                 
arcpy.env.workspace=r"E:\data_2015\Mitra\Pasta_mapeamentos_completo_2015_07_d13\Clip_split_0125"
lista_clips=arcpy.ListFeatureClasses()
lista_clips_0125=[]
for i in lista_clips:
    if "0125" in i:
        lista_clips_0125.append(i)
 
for i in lista_clips_0125:
    inpname=i.replace(".shp","")
    arcpy.AddField_management(inpname, 'AreaHA', "DOUBLE", 20, 20)
    arcpy.AddField_management(inpname, 'AreaM2', "DOUBLE", 20, 20)
    arcpy.AddField_management(inpname, 'PCT_HA', "DOUBLE", 20, 20)
    arcpy.CalculateField_management(inpname,"AreaM2","!shape.area@squaremeters!","PYTHON_9.3","#") 
    expressao='!AreaM2!/10000'
    arcpy.CalculateField_management(inpname,"AreaHA",expressao,"PYTHON_9.3","#")
    with arcpy.da.SearchCursor(inpname, "AreaHA") as cursor:
        acumula=0
        for row in cursor:
            acumula=acumula+row[0]
            expressao_PCT='!AreaHA!/'+`acumula`+"*100"
        print acumula
        arcpy.CalculateField_management(inpname,"PCT_HA",expressao_PCT,"PYTHON_9.3","#")           
              
            
        
# somando as pcts 0125

for i in lista_clips_0125:
    inpname=i.replace(".shp","")
    #arcpy.AddField_management(inpname, 'PCTSUM', "DOUBLE", 20, 20)
    lista_check_cod=[]
    with arcpy.da.SearchCursor(inpname, "codigo") as cursor:
        for row in cursor:
            if not row[0] in lista_check_cod:
                lista_check_cod.append(row[0])
            
                query="codigo=%d"%row[0]
                arcpy.SelectLayerByAttribute_management(inpname,"NEW_SELECTION",query)
                field = arcpy.da.TableToNumPyArray (inpname, "PCT_HA", skip_nulls=True)
                sum_tot = field["PCT_HA"].sum() 
                arcpy.CalculateField_management(inpname,"PCTSUM",sum_tot,"PYTHON_9.3","#")
                arcpy.SelectLayerByAttribute_management(inpname,"CLEAR_SELECTION")
#---------------------------------------------------------------------------------------------------------------------------------------------







#---------------------------------------------------------------------------------------------------------------------------------------------
# 250   calculando a PCT para a escala de 0250     
arcpy.env.workspace=r"E:\data_2015\Mitra\Pasta_mapeamentos_completo_2015_07_d13\Clip_split_0250"
lista_clips=arcpy.ListFeatureClasses()
lista_clips_0250=[]
for i in lista_clips:
    if "0250" in i:
        lista_clips_0250.append(i)
 
for i in lista_clips_0250:
    inpname=i.replace(".shp","")
    arcpy.AddField_management(inpname, 'AreaHA', "DOUBLE", 20, 20)
    arcpy.AddField_management(inpname, 'AreaM2', "DOUBLE", 20, 20)
    arcpy.AddField_management(inpname, 'PCT_HA', "DOUBLE", 20, 20)
    arcpy.CalculateField_management(inpname,"AreaM2","!shape.area@squaremeters!","PYTHON_9.3","#") 
    expressao='!AreaM2!/10000'
    arcpy.CalculateField_management(inpname,"AreaHA",expressao,"PYTHON_9.3","#")
    with arcpy.da.SearchCursor(inpname, "AreaHA") as cursor:
        acumula=0
        for row in cursor:
            acumula=acumula+row[0]
            expressao_PCT='!AreaHA!/'+`acumula`+"*100"
        print acumula
        arcpy.CalculateField_management(inpname,"PCT_HA",expressao_PCT,"PYTHON_9.3","#")    




#
        
# somando as pcts 0250

for i in lista_clips_0250:
    inpname=i.replace(".shp","")
    #arcpy.AddField_management(inpname, 'PCTSUM', "DOUBLE", 20, 20)
    lista_check_cod=[]
    with arcpy.da.SearchCursor(inpname, "codigo") as cursor:
        for row in cursor:
            if not row[0] in lista_check_cod:
                lista_check_cod.append(row[0])
            
                query="codigo=%d"%row[0]
                arcpy.SelectLayerByAttribute_management(inpname,"NEW_SELECTION",query)
                field = arcpy.da.TableToNumPyArray (inpname, "PCT_HA", skip_nulls=True)
                sum_tot = field["PCT_HA"].sum() 
                arcpy.CalculateField_management(inpname,"PCTSUM",sum_tot,"PYTHON_9.3","#")
                arcpy.SelectLayerByAttribute_management(inpname,"CLEAR_SELECTION")
    

#---------------------------------------------------------------------------------------------------------------------------------------------





# 500   calculando a PCT para a escala de 0500     
arcpy.env.workspace=r"E:\data_2015\Mitra\Pasta_mapeamentos_completo_2015_07_d13\Clip_split_0500"
lista_clips=arcpy.ListFeatureClasses()
lista_clips_500=[]
for i in lista_clips:
    if "0500" in i:
        lista_clips_500.append(i)
 
for i in lista_clips_500:
    inpname=i.replace(".shp","")
    arcpy.AddField_management(inpname, 'AreaHA', "DOUBLE", 20, 20)
    arcpy.AddField_management(inpname, 'AreaM2', "DOUBLE", 20, 20)
    arcpy.AddField_management(inpname, 'PCT_HA', "DOUBLE", 20, 20)
    arcpy.CalculateField_management(inpname,"AreaM2","!shape.area@squaremeters!","PYTHON_9.3","#") 
    expressao='!AreaM2!/10000'
    arcpy.CalculateField_management(inpname,"AreaHA",expressao,"PYTHON_9.3","#")
    with arcpy.da.SearchCursor(inpname, "AreaHA") as cursor:
        acumula=0
        for row in cursor:
            acumula=acumula+row[0]
            expressao_PCT='!AreaHA!/'+`acumula`+"*100"
        print acumula
        arcpy.CalculateField_management(inpname,"PCT_HA",expressao_PCT,"PYTHON_9.3","#")




#
# somando as pcts 0500

for i in lista_clips_500:
    inpname=i.replace(".shp","")
    #arcpy.AddField_management(inpname, 'PCTSUM', "DOUBLE", 20, 20)
    lista_check_cod=[]
    with arcpy.da.SearchCursor(inpname, "codigo") as cursor:
        for row in cursor:
            if not row[0] in lista_check_cod:
                lista_check_cod.append(row[0])
            
                query="codigo=%d"%row[0]
                arcpy.SelectLayerByAttribute_management(inpname,"NEW_SELECTION",query)
                field = arcpy.da.TableToNumPyArray (inpname, "PCT_HA", skip_nulls=True)
                sum_tot = field["PCT_HA"].sum() 
                arcpy.CalculateField_management(inpname,"PCTSUM",sum_tot,"PYTHON_9.3","#")
                arcpy.SelectLayerByAttribute_management(inpname,"CLEAR_SELECTION")
#---------------------------------------------------------------------------------------------------------------------------------------------




#---------------------------------------------------------------------------------------------------------------------------------------------

# 1000   calculando a PCT para a escala de 1000   
arcpy.env.workspace=r"E:\data_2015\Mitra\Pasta_mapeamentos_completo_2015_07_d13\Clip_split_1000"
lista_clips=arcpy.ListFeatureClasses()
lista_clips_1000=[]
for i in lista_clips:
    if "1000" in i:
        lista_clips_1000.append(i)
 
for i in lista_clips_1000:
    inpname=i.replace(".shp","")
    arcpy.AddField_management(inpname, 'AreaHA', "DOUBLE", 20, 20)
    arcpy.AddField_management(inpname, 'AreaM2', "DOUBLE", 20, 20)
    arcpy.AddField_management(inpname, 'PCT_HA', "DOUBLE", 20, 20)
    arcpy.CalculateField_management(inpname,"AreaM2","!shape.area@squaremeters!","PYTHON_9.3","#") 
    expressao='!AreaM2!/10000'
    arcpy.CalculateField_management(inpname,"AreaHA",expressao,"PYTHON_9.3","#")
    with arcpy.da.SearchCursor(inpname, "AreaHA") as cursor:
        acumula=0
        for row in cursor:
            acumula=acumula+row[0]
            expressao_PCT='!AreaHA!/'+`acumula`+"*100"
        print acumula
        arcpy.CalculateField_management(inpname,"PCT_HA",expressao_PCT,"PYTHON_9.3","#")
    
#

# somando as pcts 01000

for i in lista_clips_1000:
    inpname=i.replace(".shp","")
    arcpy.AddField_management(inpname, 'PCTSUM', "DOUBLE", 20, 20)
    lista_check_cod=[]
    with arcpy.da.SearchCursor(inpname, "codigo") as cursor:
        for row in cursor:
            if not row[0] in lista_check_cod:
                lista_check_cod.append(row[0])
            
                query="codigo=%d"%row[0]
                arcpy.SelectLayerByAttribute_management(inpname,"NEW_SELECTION",query)
                field = arcpy.da.TableToNumPyArray (inpname, "PCT_HA", skip_nulls=True)
                sum_tot = field["PCT_HA"].sum() 
                arcpy.CalculateField_management(inpname,"PCTSUM",sum_tot,"PYTHON_9.3","#")
                arcpy.SelectLayerByAttribute_management(inpname,"CLEAR_SELECTION")
            

                
#---------------------------------------------------------------------------------------------------------------------------------------------