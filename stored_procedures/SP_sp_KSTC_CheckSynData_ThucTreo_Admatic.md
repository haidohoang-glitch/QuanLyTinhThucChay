# Stored Procedure: `sp_KSTC_CheckSynData_ThucTreo_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-04-10 14:37:35.977000
- **Ngày sửa cuối**: 2020-10-10 09:31:45.067000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_CheckSynData_ThucTreo_Admatic]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	
SELECT A.*,B.*  FROM (
SELECT Contract_Id, Contract_Detail_Id, Product_Id,Id,Created_At,Last_Modified_At
FROM [asd14].ThucTreo.dbo.ThucTreo tt
WHERE 1=1 and product_formality_id = 42
--AND Id=8214
 AND Deleted_Status =0
 AND isnull(Created_At,'1900-01-01') <convert(date,getdate())
)A
FULL OUTER JOIN
--LEFT JOIN
(
SELECT ThucChayHopDongChiTietID IDtt, HopDongREF,HopDongChiTietREF,hdct.DmSanPhamREF,  ttr.DeletedStatus,ttr.CreatedAt,ttr.LastModifiedAt 
FROM dbo.ThucChayHopDongChiTiet ttr left join HopDongChiTiet hdct on hdct.HopDongChiTietID = ttr.HopDongChiTietREF
WHERE 1=1 --and ThucChayHopDongChiTietID =110966
AND ttr.CreatedAt <convert(date,getdate())
AND ttr.DeletedStatus = 0 
AND ttr.DmHinhThucQuangCaoREF = 42
and isnull(LoaiThucTreo,'') <>'ChiPhi'
)B
ON A.Id = B.IDtt
WHERE A.Id IS NULL OR B.IDtt IS NULL
--OR A.Contract_Id <> B.HopDongREF 
OR A.Contract_Detail_Id <> B.HopDongChiTietREF
ORDER BY A.Last_Modified_At,B.LastModifiedAt DESC
END

```
