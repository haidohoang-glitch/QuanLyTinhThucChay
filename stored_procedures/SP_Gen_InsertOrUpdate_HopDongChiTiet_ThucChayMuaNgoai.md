# Stored Procedure: `Gen_InsertOrUpdate_HopDongChiTiet_ThucChayMuaNgoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-12 17:05:02.873000
- **Ngày sửa cuối**: 2017-09-12 17:06:50.303000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_HopDongChiTiet_ThucChayMuaNgoai] 
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongChiTiet_ThucChayMuaNgoai] 	

As 	
BEGIN
DECLARE @NgayThucHien DATETIME
DECLARE @SQL NVARCHAR(MAX) =''
DECLARE @NgayBatDau     DATETIME
        
SET @NgayThucHien = 
	(
        SELECT MAX(dchdct.LastModifiedAt)
        FROM   dbo.HopDongChiTiet dchdct
    )

SET @NgayThucHien = DATEADD(DAY,-2,@NgayThucHien)


CREATE TABLE #HopDongChiTiet
(
	[HopDongChiTietID] [int] NOT NULL,
	[DonViTinhThucChayMuaNgoaiREF] [int] NULL,
	[DonViTinhThucChayMuaNgoai] [nvarchar](150) NULL,
	[ThanhTienThucChayMuaNgoaiTruocCK] [float] NULL,
	[ChietKhauMuaNgoai] [int] NULL,
	[STATUS] INT
)


SET @SQL = 'CALL Abm_get_hdcn_phanbosite_thucchaymuangoai (''''' + CONVERT(NVARCHAR(20), @NgayThucHien, 120)
    + ''''');'

SET @SQL = 
    'Select
    	hdct.HopDongChiTietID,
		hdct.DonViTinhThucChayMuaNgoaiREF,
		hdct.DonViTinhThucChayMuaNgoai,
		hdct.ThanhTienThucChayMuaNgoaiTruocCK,
		hdct.ChietKhauMuaNgoai,
		0
	from openquery(MYSQL,''' + @SQL + ''') hdct'

PRINT @SQL

INSERT INTO #HopDongChiTiet
EXECUTE
  (
    @SQL
  )
	UPDATE #HopDongChiTiet
    SET    [STATUS] = 1
    FROM  #HopDongChiTiet t INNER JOIN HopDongChiTiet dc
    ON t.HopDongChiTietID = dc.HopDongChiTietID

	UPDATE HopDongChiTiet
	    SET    [DonViTinhThucChayMuaNgoaiREF] = hdct.DonViTinhThucChayMuaNgoaiREF,
	           [DonViTinhThucChayMuaNgoai] = hdct.DonViTinhThucChayMuaNgoai,
			   [ThanhTienThucChayMuaNgoaiTruocCK] = hdct.ThanhTienThucChayMuaNgoaiTruocCK,
			   [ChietKhauMuaNgoai] = hdct.ChietKhauMuaNgoai
	FROM #HopDongChiTiet hdct
	    WHERE  HopDongChiTiet.[HopDongChiTietID]     = hdct.HopDongChiTietID AND hdct.[STATUS]=1

	    
 
	DROP TABLE #HopDongChiTiet

END
```
