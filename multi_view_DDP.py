import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")

for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
	mxd.dataDrivenPages.currentPageID = pageNum
	pageorder = mxd.dataDrivenPages.pageRow.yourfieldonDDP
	arcpy.mapping.ExportToPNG(mxd, r"E:\GBSM_NDVI\2018\ANALISA_NDVI\JPEG/" + str(pageNum) +"_"+ pageorder + ".png")

##janganlupa extent framenya dinyalakan kalau mau double view
