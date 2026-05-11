# Stored Procedure: `sp_KSTC_CheckIdNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-15 11:31:47.910000
- **Ngày sửa cuối**: 2021-04-19 11:37:38.997000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_CheckIdNhanHang]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here

	-- 1 Nhãn treo branding
	--select top 1 * from [[asd14]].thuctreo.dbo.thuctreo_pr
	Select N'Nhãn treo Branding' [Nhom], treobrand.Contract_Id, treobrand.Dm_NhanHang_Id
,treobrand.TenNhanHang nhantreo
,nhanhang.TenNhanHang
,nhanhang.DmNhanHangID,treobrand.Last_Modified_At 
from [192.168.23.150].thuctreo.dbo.thuctreo treobrand
inner join [192.168.23.150].BRAND.DBO.DMNHANHANG nhanhang
ON treobrand.Dm_NhanHang_Id= nhanhang.DmNhanHangID
where 1=1
AND treobrand.Deleted_Status = 0 
AND treobrand.Last_Modified_At >='2020-01-01'
and (treobrand.Dm_NhanHang_Id is null or  nhanhang.DmNhanHangID is null)
/*AND NOT LTRIM(RTRIM(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(treobrand.TenNhanHang,CHAR(10),'[]'),CHAR(13),'[]'),char(9),'[]'),CHAR(32),'[]'),'][',''),'[]',CHAR(32)))) =
LTRIM(RTRIM(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(nhanhang.TenNhanHang,CHAR(10),'[]'),CHAR(13),'[]'),char(9),'[]'),CHAR(32),'[]'),'][',''),'[]',CHAR(32)))) 
*/
order by treobrand.Last_Modified_At desc

	-- 2.Nhãn treo chi phí
	Select N'Nhãn treo chi phí' [Nhom],chiphi.Contract_Id,chiphi.Contract_detail_id, chiphi.Product_id,chiphi.product_formality_id, chiphi.Brand_Id
,chiphi.Brand_Name
,nhanhang.TenNhanHang
,nhanhang.DmNhanHangID,chiphi.Id,chiphi.LastmodifiedAt
from [192.168.23.150].thuctreo.dbo.thuctreo_chiphi chiphi
inner join [192.168.23.150].BRAND.DBO.DMNHANHANG nhanhang
ON chiphi.Brand_Id= nhanhang.DmNhanHangID
where chiphi.DeletedStatus = 0 and chiphi.LastmodifiedAt >='2020-01-01'
AND Not LTRIM(RTRIM(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(chiphi.Brand_Name,CHAR(10),'[]'),CHAR(13),'[]'),char(9),'[]'),CHAR(32),'[]'),'][',''),'[]',CHAR(32)))) =
LTRIM(RTRIM(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(nhanhang.TenNhanHang,CHAR(10),'[]'),CHAR(13),'[]'),char(9),'[]'),CHAR(32),'[]'),'][',''),'[]',CHAR(32)))) 
order by chiphi.LastmodifiedAt desc
  -- 3.Nhãn treo PR
  	Select N'Nhãn treo PR' [Nhom],pr.Contract_Id,pr.NhanHang_Id
,pr.TenNhanHang
,nhanhang.TenNhanHang
,nhanhang.DmNhanHangID,pr.Last_modified_At
from [192.168.23.150].thuctreo.dbo.thuctreo_PR pr
inner join [192.168.23.150].BRAND.DBO.DMNHANHANG nhanhang
ON pr.NhanHang_Id= nhanhang.DmNhanHangID
where pr.Deleted_Status = 0 and pr.Last_modified_At >='2020-01-01'
and (pr.NhanHang_Id is null or  nhanhang.DmNhanHangID is null)
/*AND Not LTRIM(RTRIM(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(pr.TenNhanHang,CHAR(10),'[]'),CHAR(13),'[]'),char(9),'[]'),CHAR(32),'[]'),'][',''),'[]',CHAR(32)))) =
LTRIM(RTRIM(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(nhanhang.TenNhanHang,CHAR(10),'[]'),CHAR(13),'[]'),char(9),'[]'),CHAR(32),'[]'),'][',''),'[]',CHAR(32)))) 
*/order by pr.Last_modified_At desc
END

```
