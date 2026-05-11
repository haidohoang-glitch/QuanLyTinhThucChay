# Stored Procedure: `Gen_InsertOrUpdate_INFOBANNER_BRANDING_THANHTIEN_ADMATIC`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-23 16:04:07.277000
- **Ngày sửa cuối**: 2022-12-21 14:24:05.810000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_INFOBANNER_BRANDING_THANHTIEN_ADMATIC] 
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_INFOBANNER_BRANDING_THANHTIEN_ADMATIC] 	
As 	
BEGIN


DECLARE @NgayThucHien DATETIME
DECLARE @SQL NVARCHAR(MAX)
SET @NgayThucHien = 
	(
        SELECT MAX(dchdct.LastModifiedAt)
        FROM   [dbo].[INFOBANNER_BRANDING_THANHTIEN_ADMATIC] dchdct
    )

	SET @NgayThucHien = DATEADD(HOUR,-8,@NgayThucHien)
	SET @NgayThucHien = '2022-06-21'
	--PRINT @NgayThucHien
	CREATE TABLE #INFOBANNER_BRANDING_THANHTIEN_ADMATIC(
		[ID] [int] NOT NULL,
		[SOHOPDONG] [nvarchar](50) NULL,
		[DMSANPHAMREF] [int] NULL,
		[DMBANNERREF] [int] NULL,
		[CREATEDAT] [datetime] NULL,
		[CREATEDBY] [nvarchar](50) NULL,
		[LASTMODIFIEDAT] [datetime] NULL,
		[LASTMODIFIEDBY] [nvarchar](50) NULL,
		[DELETEDSTATUS] [smallint] NULL,
		[TrangThaiTinh] [smallint] NULL,
		[NgayThucHienMax] [datetime] NULL,
		[STATUS] SMALLINT
	) 

	INSERT INTO #INFOBANNER_BRANDING_THANHTIEN_ADMATIC
           ([ID]
           ,[SOHOPDONG]
           ,[DMSANPHAMREF]
           ,[DMBANNERREF]
           ,[CREATEDAT]
           ,[CREATEDBY]
           ,[LASTMODIFIEDAT]
           ,[LASTMODIFIEDBY]
           ,[DELETEDSTATUS]
           ,[TrangThaiTinh]
           ,[NgayThucHienMax]
		   ,[STATUS])


		SELECT tc.ThucChayHopDongChiTietID, hd.SoHopDong, tc.DmSanPhamREF
		, tc.DmBannerREF, tc.CreatedAt, tc.CreatedBy
		, tc.LastModifiedAt, tc.LastModifiedBy
		, tc.DeletedStatus, tc.TrangThaiTinh
		, tc.NgayThucHienMax 
		, 0 status_record
		FROM
		(
			SELECT tc.ThucChayHopDongChiTietID
			, tc.HopDongREF
			, tc.DmSanPhamREF
			, tc.DmBannerREF
			, tc.CreatedAt
			, tc.CreatedBy
			, tc.LastModifiedAt
			, tc.LastModifiedBy
			, tc.DeletedStatus
			, 0 AS TrangThaiTinh
			, '1900-01-01' AS NgayThucHienMax FROM dbo.ThucChayHopDongChiTiet tc
			WHERE tc.DmHinhThucQuangCaoREF = 42
			AND tc.CreatedBy = N'BrandingTool'
			AND tc.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,821,342,585,140,228,564,549,5082,5133,5056,5268) --HAIDH COMMENT THEM SANPHAM 5133 NGÀY 26/10/2021
			AND CONVERT(DATE,tc.LastModifiedAt) >= @NgayThucHien
		)tc
		INNER JOIN dbo.HopDong hd on tc.HopDongREF = hd.HopDongID


		UPDATE t 
		SET    [STATUS] = 1
		FROM  #INFOBANNER_BRANDING_THANHTIEN_ADMATIC t INNER JOIN dbo.INFOBANNER_BRANDING_THANHTIEN_ADMATIC dc
		ON t.SOHOPDONG = dc.SOHOPDONG AND t.DMSANPHAMREF = dc.DMSANPHAMREF
		AND t.DMBANNERREF = dc.DMBANNERREF


		-- Update nhung row da ton ton                                      

		UPDATE dc
		   SET dc.[ID] = t.ID
			  ,[CREATEDAT] = t.CREATEDAT
			  ,[CREATEDBY] = t.CREATEDBY
			  ,[LASTMODIFIEDAT] = t.LASTMODIFIEDAT
			  ,[LASTMODIFIEDBY] = t.LASTMODIFIEDBY
			  ,[DELETEDSTATUS] = t.DELETEDSTATUS
		FROM  dbo.INFOBANNER_BRANDING_THANHTIEN_ADMATIC dc INNER JOIN  #INFOBANNER_BRANDING_THANHTIEN_ADMATIC t 
		ON t.SOHOPDONG = dc.SOHOPDONG AND t.DMSANPHAMREF = dc.DMSANPHAMREF
		AND t.DMBANNERREF = dc.DMBANNERREF
		WHERE t.[STATUS] = 1


		-- Insert Row chua ton tai

		INSERT INTO dbo.INFOBANNER_BRANDING_THANHTIEN_ADMATIC
			   ([ID]
			   ,[SOHOPDONG]
			   ,[DMSANPHAMREF]
			   ,[DMBANNERREF]
			   ,[CREATEDAT]
			   ,[CREATEDBY]
			   ,[LASTMODIFIEDAT]
			   ,[LASTMODIFIEDBY]
			   ,[DELETEDSTATUS]
			   ,[TrangThaiTinh]
			   ,[NgayThucHienMax])
		

		SELECT dchdct.[ID]
			   ,dchdct.[SOHOPDONG]
			   ,dchdct.[DMSANPHAMREF]
			   ,dchdct.[DMBANNERREF]
			   ,dchdct.[CREATEDAT]
			   ,dchdct.[CREATEDBY]
			   ,dchdct.[LASTMODIFIEDAT]
			   ,dchdct.[LASTMODIFIEDBY]
			   ,dchdct.[DELETEDSTATUS]
			   ,dchdct.[TrangThaiTinh]
			   ,dchdct.[NgayThucHienMax]
		FROM #INFOBANNER_BRANDING_THANHTIEN_ADMATIC dchdct 
		WHERE dchdct.[STATUS]=0

		DROP TABLE #INFOBANNER_BRANDING_THANHTIEN_ADMATIC

END

```
