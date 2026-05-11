# Stored Procedure: `Gen_InsertOrUpdate_ThucChayMuaNgoai_HopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-03 16:26:57.060000
- **Ngày sửa cuối**: 2017-11-03 16:38:27.187000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayMuaNgoai_HopDongChiTiet] 	
As 	
DECLARE @NgayThucHien DATETIME
DECLARE @SQL NVARCHAR(MAX)
SET @NgayThucHien = 
ISNULL((
        SELECT MAX(dchdct.LastModifiedAt)
        FROM   ThucChayMuaNgoai_HopDongChiTiet dchdct
    ),'2010-01-01')

set @NgayThucHien = DATEADD(day,-1,@NgayThucHien)

PRINT @NgayThucHien

CREATE TABLE #ThucChayMuaNgoai_HopDongChiTiet(
	[HopDongChiTietREF] [int] NOT NULL,
	[HopDongREF] [int] NOT NULL,
	[SoLuongThucChay] [int] NULL,
	[DonViTinhThucChayMuaNgoaiREF] [int] NULL,
	[DonViTinhThucChayMuaNgoai] [nvarchar](200) NULL,
	[ThanhTienThucChayMuaNgoaiTruocCK] [bigint] NULL,
	[ChietKhauMuaNgoai] [float] NULL,
	[NgaySuaThucChay] [datetime] NULL,
	[NguoiSuaThucChay] [varchar](200) NULL,
	[CreatedBy] [varchar](50) NULL,
	[CreatedAt] [datetime] NULL,
	[LastModifiedBy] [varchar](50) NULL,
	[LastModifiedAt] [datetime] NULL,
	[DeletedStatus] [int] NOT NULL,
	[PrintStatus] [int] NOT NULL,
	[RecordStatus] [int] NOT NULL,
	Status int
) 

SET @SQL = 
    '
SELECT 
	 tchdctp.HopDongChiTietID,
     tchdctp.HopDongFK,
     tchdctp.SoLuongThucChay,
     tchdctp.DonViTinhThucChayMuaNgoaiREF,
     tchdctp.DonViTinhThucChayMuaNgoai,
     tchdctp.ThanhTienThucChayMuaNgoaiTruocCK,
     tchdctp.ChietKhauMuaNgoai,
	 tchdctp.NgaySuaThucChay, 
     tchdctp.NguoiSuaThucChay ,
     tchdctp.CreatedBy,
     tchdctp.CreatedAt,
     tchdctp.LastModifiedBy,
     tchdctp.LastModifiedAt,
     tchdctp.DeletedStatus,
     tchdctp.PrintStatus,
     tchdctp.RecordStatus,
     0
FROM OPENQUERY(MySQL,''CALL Abm_get_hdcn_phanbosite_thucchaymuangoai (''''' + CONVERT(NVARCHAR(50), @NgayThucHien, 120)
    + ''''');'') tchdctp'


PRINT @SQL
INSERT INTO #ThucChayMuaNgoai_HopDongChiTiet
EXECUTE
  (
    @SQL
  )
--DROP TABLE #HopDongChiTiet_MuaNgoai
   -- Set trang thai = 1 doi voi nhung truong hop sua chua 
    UPDATE #ThucChayMuaNgoai_HopDongChiTiet
    SET    [STATUS] = 1
    FROM  #ThucChayMuaNgoai_HopDongChiTiet t INNER JOIN dbo.ThucChayMuaNgoai_HopDongChiTiet  dc
    ON t.HopDongChiTietREF = dc.HopDongChiTietREF

-- Update nhung row da ton ton                                      
  UPDATE [dbo].[ThucChayMuaNgoai_HopDongChiTiet]
   SET [SoLuongThucChay] = A.SoLuongThucChay
      ,[DonViTinhThucChayMuaNgoaiREF] = A.DonViTinhThucChayMuaNgoaiREF
      ,[DonViTinhThucChayMuaNgoai] = A.DonViTinhThucChayMuaNgoai
      ,[ThanhTienThucChayMuaNgoaiTruocCK] = A.ThanhTienThucChayMuaNgoaiTruocCK
      ,[ChietKhauMuaNgoai] = A.ChietKhauMuaNgoai
      ,[NgaySuaThucChay] = A.NgaySuaThucChay
      ,[NguoiSuaThucChay] = A.NguoiSuaThucChay
      ,[LastModifiedBy] = A.LastModifiedBy
      ,[LastModifiedAt] = A.LastModifiedAt
    
    FROM   #ThucChayMuaNgoai_HopDongChiTiet A 
    WHERE  [STATUS] = 1 AND A.HopDongChiTietREF = [ThucChayMuaNgoai_HopDongChiTiet].HopDongChiTietREF
-- Insert Row chua ton tai
INSERT INTO [dbo].ThucChayMuaNgoai_HopDongChiTiet
SELECT [HopDongChiTietREF]
      ,[HopDongREF]
      ,[SoLuongThucChay]
      ,[DonViTinhThucChayMuaNgoaiREF]
      ,[DonViTinhThucChayMuaNgoai]
      ,[ThanhTienThucChayMuaNgoaiTruocCK]
      ,[ChietKhauMuaNgoai]
      ,[NgaySuaThucChay]
      ,[NguoiSuaThucChay]
      ,[CreatedBy]
      ,[CreatedAt]
      ,[LastModifiedBy]
      ,[LastModifiedAt]
      ,[DeletedStatus]
      ,[PrintStatus]
      ,[RecordStatus]

FROM #ThucChayMuaNgoai_HopDongChiTiet   dchdct WHERE dchdct.[STATUS]=0



```
