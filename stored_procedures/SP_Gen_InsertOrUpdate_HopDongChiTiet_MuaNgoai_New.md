# Stored Procedure: `Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_New`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-26 16:19:28.357000
- **Ngày sửa cuối**: 2019-05-13 10:33:21.873000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_New]
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_New]
As 	
BEGIN
    DECLARE @NgayThucHien DATETIME, @NgayThucHien_ThucChayMN DATETIME
	, @NgayThucHien_HDCT DATETIME
	DECLARE @SQL NVARCHAR(MAX), @SQL_ThucChayMN NVARCHAR(MAX) = ''

	-----------------CHECK HOPDONGCHITIET, THANHTIEN THAY DOI, UPDATE THUCCHAYBAN ---------------
	SET @NgayThucHien_HDCT = DATEADD(DAY,-2, CONVERT(DATE,GETDATE()))
	--CAP NHAT THANHTIENBANSAUCK VA THANHTIENLAISAUCK CUA DU TOAN MUA NGOAI HOPDONGCHITIET_MUANGOAI
	UPDATE dbo.HopDongChiTiet_MuaNgoai
	SET ThanhTienBanSauCK = hdct.ThanhTien
	, ThanhTienLaiSauCK = (hdct.ThanhTien - mn.ThanhTienSauCKMua)
	FROM dbo.HopDongChiTiet_MuaNgoai mn
	INNER JOIN 
	(SELECT hdct.HopDongChiTietID, hdct.ThanhTien, hdct.HopDongFK
		, hdct.DmLoaiREF, hdct.DmLoaiBannerREF 
		FROM dbo.HopDongChiTiet hdct 
		WHERE hdct.DeletedStatus = 0 
		AND (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)
		AND CONVERT(DATE,hdct.LastModifiedAt) >= @NgayThucHien_HDCT
	)hdct ON mn.HopDongChiTietID = hdct.HopDongChiTietID

	--CAP NHAT CHIETKHAU MUANGOAI, THANHTIENLAIMUANGOAI, THUCCHAYBANMUANGOAI TREN THUCCHAYMUANGOAICHITIET
	UPDATE dbo.ThucChayMuaNgoaiChiTiet
	SET ChietKhauMuaNgoai = hdct.ChietKhauMua
	FROM dbo.ThucChayMuaNgoaiChiTiet mn
	INNER JOIN dbo.HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID

	UPDATE dbo.ThucChayMuaNgoaiChiTiet
	SET ThanhTienLaiThucChaySauCK = CASE WHEN hdct.ThanhTienSauCKMua <> 0 THEN hdct.ThanhTienLaiSauCK*((mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)/hdct.ThanhTienSauCKMua)
									ELSE 0
									END
	FROM  dbo.ThucChayMuaNgoaiChiTiet mn
	INNER JOIN dbo.HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID

	UPDATE dbo.ThucChayMuaNgoaiChiTiet
	SET ThanhTienThucChayBanSauCK = mn.ThanhTienLaiThucChaySauCK + (mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)
	FROM dbo.ThucChayMuaNgoaiChiTiet mn
	INNER JOIN dbo.HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID
	-------------------END THANHTIEN HDCT------------------------------

	SET @NgayThucHien = 
	ISNULL((
			SELECT MAX(dchdct.LastModifiedAt)
			FROM   DBO.HopDongChiTiet_MuaNgoai dchdct
		),'2010-01-01')

	set @NgayThucHien = DATEADD(day,-1,@NgayThucHien)

	PRINT @NgayThucHien
	---------------------HOPDONGCHITIET_MUANGOAI DU TOAN MUA NGOAI------------------------------
	CREATE TABLE #HopDongChiTiet_MuaNgoai(
		[HopDongChiTietID] [int] NOT NULL,
		[SoHopDongMua] [nvarchar](30) NULL,
		[DonGiaMua] [decimal](20, 0) NULL,
		[SoLuongMua] [float] NULL,
		[DonViTinh] [int] NULL,
		[SoLuongText] [nvarchar](1) NULL,
		[ChietKhauMua] [float] NULL,
		[ThanhTienSauCKMua] [decimal](20, 0) NULL,
		[VAT] [decimal](10, 0) NULL,
		[AttachFile] [nvarchar](500) NULL,
		[CreatedAt] [datetime] NULL,
		[CreatedBy] [nvarchar](30) NULL,
		[LastModifiedAt] [datetime] NULL,
		[LastModifiedBy] [nvarchar](30) NULL,
		[DeletedStatus] [smallint] NULL,
		[ThanhTienBanSauCK] [float] NULL,
		[ThanhTienLaiSauCK] [float] NULL,
		STATUS INT
	)

	SET @SQL = 
		'
	SELECT 
		hdctmn.PhanBoSiteID,
		hdctmn.SoHopDongMua,
		hdctmn.DonGiaMua,
		hdctmn.SoLuongMua,
		hdctmn.DonViTinh,
		hdctmn.SoLuongText,
		hdctmn.ChietKhauMua,
		hdctmn.ThanhTienSauCKMua,
		hdctmn.VAT,
		hdctmn.AttachFile,
		CASE WHEN CONVERT(NVARCHAR(40),hdctmn.CreatedAt)<=''1900-01-01'' THEN ''1900-01-01'' ELSE CONVERT(DATETIME,hdctmn.CreatedAt) END,
		hdctmn.CreatedBy,
		CASE WHEN CONVERT(NVARCHAR(40),hdctmn.LastModifiedAt)<=''1900-01-01'' THEN ''1900-01-01'' ELSE CONVERT(DATETIME,hdctmn.LastModifiedAt) END,
		hdctmn.LastModifiedBy,
		hdctmn.DeletedStatus,
		0 AS ThanhTienBanSauCK,
		0 AS ThanhTienLaiSauCK,
		0
	FROM OPENQUERY(MySQL,''SELECT * FROM hdcn_phanbosite_muangoai WHERE LastModifiedAt >= (''''' + CONVERT(NVARCHAR(50), @NgayThucHien, 120)
		+ ''''');'') hdctmn'

	PRINT @SQL
	INSERT INTO #HopDongChiTiet_MuaNgoai
	EXECUTE
	  (
		@SQL
	  )

	-- Set trang thai = 1 doi voi nhung truong hop sua chua 
	UPDATE #HopDongChiTiet_MuaNgoai
		SET    [STATUS] = 1
		FROM  #HopDongChiTiet_MuaNgoai t INNER JOIN HopDongChiTiet_MuaNgoai  dc
		ON t.HopDongChiTietID = dc.HopDongChiTietID

	--CAP NHAT THANHTIENBANSAUCK VA THANHTIENLAISAUCK CUA DU TOAN MUA NGOAI
	UPDATE #HopDongChiTiet_MuaNgoai
	SET ThanhTienBanSauCK = hdct.ThanhTien
	, ThanhTienLaiSauCK = (hdct.ThanhTien - mn.ThanhTienSauCKMua)
	FROM #HopDongChiTiet_MuaNgoai mn
	INNER JOIN dbo.HopDongChiTiet hdct ON mn.HopDongChiTietID = hdct.HopDongChiTietID

	-- UPDATE GIA TRI CHO NHUNG BAN GHI DA TON TAI                                      
	   UPDATE DBO.HopDongChiTiet_MuaNgoai
		SET
			HopDongChiTietID = A.HopDongChiTietID,
			SoHopDongMua = A.SoHopDongMua,
			DonGiaMua = A.DonGiaMua,
			SoLuongMua = A.SoLuongMua,
			DonViTinh = A.DonViTinh,
			SoLuongText = A.SoLuongText,
			ChietKhauMua = A.ChietKhauMua,
			ThanhTienSauCKMua = A.ThanhTienSauCKMua,
			VAT = A.VAT,
			AttachFile = A.AttachFile,
			CreatedAt = A.CreatedAt,
			CreatedBy = A.CreatedBy,
			LastModifiedAt = A.LastModifiedAt,
			LastModifiedBy = A.LastModifiedBy,
			DeletedStatus = A.DeletedStatus,
			ThanhTienBanSauCK = A.ThanhTienBanSauCK,
			ThanhTienLaiSauCK = A.ThanhTienLaiSauCK
		FROM   #HopDongChiTiet_MuaNgoai A 
		WHERE  [STATUS] = 1 AND A.HopDongChiTietID = HopDongChiTiet_MuaNgoai.HopDongChiTietID
	-- INSERT ROW CHUA TON TAI
	INSERT INTO [dbo].HopDongChiTiet_MuaNgoai
	(
	    HopDongChiTietID,
	    SoHopDongMua,
	    DonGiaMua,
	    SoLuongMua,
	    DonViTinh,
	    SoLuongText,
	    ChietKhauMua,
	    ThanhTienSauCKMua,
	    VAT,
	    AttachFile,
	    CreatedAt,
	    CreatedBy,
	    LastModifiedAt,
	    LastModifiedBy,
	    DeletedStatus,
		ThanhTienBanSauCK,
		ThanhTienLaiSauCK
	)
	
	      
	SELECT dchdct.HopDongChiTietID, dchdct.SoHopDongMua, dchdct.DonGiaMua,
		   dchdct.SoLuongMua, dchdct.DonViTinh, dchdct.SoLuongText,
		   dchdct.ChietKhauMua, dchdct.ThanhTienSauCKMua, dchdct.VAT,
		   dchdct.AttachFile, dchdct.CreatedAt, dchdct.CreatedBy,
		   dchdct.LastModifiedAt, dchdct.LastModifiedBy, dchdct.DeletedStatus,
		   dchdct.ThanhTienBanSauCK, dchdct.ThanhTienLaiSauCK
	FROM #HopDongChiTiet_MuaNgoai   dchdct WHERE dchdct.[STATUS]=0

	--CAP NHAT THANHTIENBANSAUCK VA THANHTIENLAISAUCK CUA DU TOAN MUA NGOAI
	UPDATE dbo.ThucChayMuaNgoaiChiTiet
	SET ChietKhauMuaNgoai = hdct.ChietKhauMua
	FROM dbo.ThucChayMuaNgoaiChiTiet mn
	INNER JOIN #HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID

	UPDATE dbo.ThucChayMuaNgoaiChiTiet
	SET ThanhTienLaiThucChaySauCK = CASE WHEN hdct.ThanhTienSauCKMua <> 0 THEN hdct.ThanhTienLaiSauCK*((mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)/hdct.ThanhTienSauCKMua)
									ELSE 0
									END
	FROM  dbo.ThucChayMuaNgoaiChiTiet mn
	INNER JOIN #HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID

	UPDATE dbo.ThucChayMuaNgoaiChiTiet
	SET ThanhTienThucChayBanSauCK = mn.ThanhTienLaiThucChaySauCK + (mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)
	FROM dbo.ThucChayMuaNgoaiChiTiet mn
	INNER JOIN #HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID

	---------------------THUCCHAYMUANGOAICHITIET THUC CHAY MUA NGOAI------------------------------

	SET @NgayThucHien_ThucChayMN = 
	ISNULL((
			SELECT MAX(dchdct.LastModifiedAt)
			FROM   dbo.ThucChayMuaNgoaiChiTiet dchdct
		),'2010-01-01')

	set @NgayThucHien_ThucChayMN = DATEADD(day,-1,@NgayThucHien_ThucChayMN)
	
	PRINT @NgayThucHien_ThucChayMN

	CREATE TABLE #ThucChayMuaNgoaiChiTiet(
		[ThucChayMuaNgoaiChiTietID] [int] NOT NULL,
		[HopDongREF] [int] NOT NULL,
		[HopDongChiTietREF] [int] NOT NULL,
		[TuNgay] [datetime] NULL,
		[DenNgay] [datetime] NULL,
		[NgayThucChay] [datetime] NULL,
		[SoLuongThucChay] [float] NULL,
		[DmDonViTinhREF] [int] NULL,
		[ChietKhauMuaNgoai] [float] NULL,
		[ThanhTienMuaNgoaiTruocCK] [float] NULL,
		[ThanhTienThucChayBanSauCK] [float] NULL,
		[ThanhTienLaiThucChaySauCK] [float] NULL,
		[CreatedAt] [datetime] NULL,
		[CreatedBy] [nvarchar](50) NULL,
		[LastModifiedAt] [datetime] NULL,
		[LastModifiedBy] [nvarchar](50) NULL,
		[Status_approved] [smallint] NULL,
		[DeletedStatus] [smallint] NULL,
		[STATUS_MN] INT
	)

	SET @SQL_ThucChayMN = 
		'
	SELECT tcmn.Id AS ThucChayMuaNgoaiChiTietID ,
		tcmn.HopDongId AS HopDongREF,
		tcmn.PhanBoId AS HopDongChiTietREF,
		(CASE WHEN ISNULL(tcmn.TuNgay,''1900-01-01'') = ''0001-01-01'' THEN ''1900-01-01''
		ELSE ISNULL(tcmn.TuNgay,''1900-01-01'')
		END)  AS TuNgay,
		(CASE WHEN ISNULL(tcmn.DenNgay,''1900-01-01'') = ''0001-01-01'' THEN ''1900-01-01''
		ELSE ISNULL(tcmn.DenNgay,''1900-01-01'')
		END) AS DenNgay,
		(CASE WHEN ISNULL(tcmn.NgayThucChay,''1900-01-01'') = ''0001-01-01'' THEN ''1900-01-01''
		ELSE ISNULL(tcmn.NgayThucChay,''1900-01-01'')
		END)  AS NgayThucChay,
		tcmn.SoLuong AS SoLuongThucChay,
		tcmn.DonViTinh AS DmDonViTinhREF,
		ISNULL(tcmn.ChietKhau,0) AS ChietKhauMuaNgoai,
		tcmn.ThanhTien AS ThanhTienThucChayMuaTruocCK,
		0 AS ThanhTienThucChayBanSauCK,
		0 AS ThanhTienLaiThucChaySauCK,
		tcmn.CreatedDate AS CreatedAt,
		tcmn.CreatedBy AS CreatedBy,
		ISNULL(tcmn.LastModifiedDate, tcmn.NgayThucChay) AS LastModifiedAt,
		ISNULL(tcmn.LastModifiedBy,tcmn.CreatedBy) AS LastModifiedBy,
		tcmn.RecordStatus AS Status_approved,
		tcmn.Deleted AS DeletedStatus,
		0 
		FROM OPENQUERY(MySQL,''SELECT * FROM hdcn_thucchay_muangoai_chitiet  WHERE LastModifiedDate >= (''''' + CONVERT(NVARCHAR(50), @NgayThucHien_ThucChayMN, 120)
		+ ''''');'') tcmn'

	PRINT @SQL_ThucChayMN
	INSERT INTO #ThucChayMuaNgoaiChiTiet
	(
	    ThucChayMuaNgoaiChiTietID,
	    HopDongREF,
	    HopDongChiTietREF,
	    TuNgay,
	    DenNgay,
	    NgayThucChay,
	    SoLuongThucChay,
	    DmDonViTinhREF,
	    ChietKhauMuaNgoai,
	    ThanhTienMuaNgoaiTruocCK,
	    ThanhTienThucChayBanSauCK,
	    ThanhTienLaiThucChaySauCK,
	    CreatedAt,
	    CreatedBy,
	    LastModifiedAt,
	    LastModifiedBy,
	    Status_approved,
	    DeletedStatus,
	    [STATUS_MN]
	)
	
	EXECUTE
	  (
		@SQL_ThucChayMN
	  )

	  --DROP TABLE #HopDongChiTiet_MuaNgoai
	   -- Set trang thai = 1 doi voi nhung truong hop sua chua 
	UPDATE t
	SET t.[STATUS_MN] = 1
	, t.NgayThucChay = (CASE WHEN t.NgayThucChay = '1900-01-01' AND t.TuNgay <> '1900-01-01' THEN t.TuNgay
	WHEN t.NgayThucChay = '1900-01-01' AND t.TuNgay = '1900-01-01' THEN CONVERT(DATE,t.CreatedAt)
	ELSE CONVERT(DATE,t.CreatedAt)
	END)
	FROM  #ThucChayMuaNgoaiChiTiet t INNER JOIN dbo.ThucChayMuaNgoaiChiTiet  dc
	ON t.ThucChayMuaNgoaiChiTietID = dc.ThucChayMuaNgoaiChiTietID
		
	--CAP NHAT THANHTIENBANSAUCK VA THANHTIENLAISAUCK CUA DU TOAN MUA NGOAI
	UPDATE #ThucChayMuaNgoaiChiTiet
	SET ChietKhauMuaNgoai = hdct.ChietKhauMua
	FROM #ThucChayMuaNgoaiChiTiet mn
	INNER JOIN dbo.HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID

	UPDATE #ThucChayMuaNgoaiChiTiet
	SET ThanhTienLaiThucChaySauCK = CASE WHEN hdct.ThanhTienSauCKMua <> 0 THEN hdct.ThanhTienLaiSauCK*((mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)/hdct.ThanhTienSauCKMua)
									ELSE 0
									END
	FROM #ThucChayMuaNgoaiChiTiet mn
	INNER JOIN dbo.HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID

	UPDATE #ThucChayMuaNgoaiChiTiet
	SET ThanhTienThucChayBanSauCK = mn.ThanhTienLaiThucChaySauCK + (mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)
	FROM #ThucChayMuaNgoaiChiTiet mn
	INNER JOIN dbo.HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID

	-- UPDATE GIA TRI CHO NHUNG BAN GHI DA TON TAI                                      

	UPDATE [dbo].[ThucChayMuaNgoaiChiTiet]
	SET [ThucChayMuaNgoaiChiTietID] = A.ThucChayMuaNgoaiChiTietID
      ,[HopDongREF] = A.HopDongREF
      ,[HopDongChiTietREF] = A.HopDongChiTietREF
      ,[TuNgay] = A.TuNgay
      ,[DenNgay] = A.DenNgay
      ,[NgayThucChay] = A.NgayThucChay
      ,[SoLuongThucChay] = A.SoLuongThucChay
      ,[DmDonViTinhREF] = A.DmDonViTinhREF
      ,[ChietKhauMuaNgoai] = A.ChietKhauMuaNgoai
      ,[ThanhTienMuaNgoaiTruocCK] = A.ThanhTienMuaNgoaiTruocCK
      ,[ThanhTienThucChayBanSauCK] = A.ThanhTienThucChayBanSauCK
      ,[ThanhTienLaiThucChaySauCK] = A.ThanhTienLaiThucChaySauCK
      ,[CreatedAt] = A.CreatedAt
      ,[CreatedBy] = A.CreatedBy
      ,[LastModifiedAt] = A.LastModifiedAt
      ,[LastModifiedBy] = A.LastModifiedBy
	  ,[Status]  = A.Status_approved
      ,[DeletedStatus] = A.DeletedStatus
 	FROM   #ThucChayMuaNgoaiChiTiet A 
		WHERE  [STATUS_MN] = 1 AND A.[ThucChayMuaNgoaiChiTietID] = [ThucChayMuaNgoaiChiTiet].ThucChayMuaNgoaiChiTietID

	--INSERT ROW CHUA TON TAI
	INSERT INTO [dbo].[ThucChayMuaNgoaiChiTiet]
           ([ThucChayMuaNgoaiChiTietID]
           ,[HopDongREF]
           ,[HopDongChiTietREF]
           ,[TuNgay]
           ,[DenNgay]
           ,[NgayThucChay]
           ,[SoLuongThucChay]
           ,[DmDonViTinhREF]
           ,[ChietKhauMuaNgoai]
           ,[ThanhTienMuaNgoaiTruocCK]
           ,[ThanhTienThucChayBanSauCK]
           ,[ThanhTienLaiThucChaySauCK]
           ,[CreatedAt]
           ,[CreatedBy]
           ,[LastModifiedAt]
           ,[LastModifiedBy]
           ,[Status]
           ,[DeletedStatus]
		   ,[TrangThaiTinhThucChay])
   
	
		      
	SELECT   ThucChayMuaNgoaiChiTietID,
	    HopDongREF,
	    HopDongChiTietREF,
	    TuNgay,
	    DenNgay,
	    NgayThucChay,
	    SoLuongThucChay,
	    DmDonViTinhREF,
	    ChietKhauMuaNgoai,
	    ThanhTienMuaNgoaiTruocCK,
	    ThanhTienThucChayBanSauCK,
	    ThanhTienLaiThucChaySauCK,
	    CreatedAt,
	    CreatedBy,
	    LastModifiedAt,
	    LastModifiedBy,
	    Status_approved,
	    DeletedStatus,
		0 TrangThaiTinhThucChay FROM #ThucChayMuaNgoaiChiTiet
		WHERE [STATUS_MN] = 0


END



```
