# Stored Procedure: `Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_New_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-08-23 09:58:07.937000
- **Ngày sửa cuối**: 2019-09-05 09:46:09.447000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_New_dev]
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_New_dev]
As 	
BEGIN
    DECLARE @NgayThucHien DATETIME, @NgayThucHien_ThucChayMN DATETIME
	DECLARE @SQL NVARCHAR(MAX), @SQL_ThucChayMN NVARCHAR(MAX) = ''

	SET @NgayThucHien = 
	ISNULL((
			SELECT MAX(dchdct.LastModifiedAt)
			FROM   DBO.HopDongChiTiet_MuaNgoai_dev dchdct
		),'2010-01-01')

	set @NgayThucHien = DATEADD(day,-1,@NgayThucHien)

	PRINT @NgayThucHien
	---------------------HOPDONGCHITIET_MUANGOAI DU TOAN MUA NGOAI------------------------------
	CREATE TABLE #HopDongChiTiet_MuaNgoai_dev(
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

	INSERT INTO #HopDongChiTiet_MuaNgoai_dev
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
	    ThanhTienLaiSauCK,
	    STATUS
	)
	
	SELECT ct.PhanBoId
	, '' AS SoHopDongMua
	, SUM(cth.DonGiaMua)/COUNT(cth.Id) AS DonGiaMua
	, SUM(cth.SoLuongMua) AS SoLuongMua
	, 0 AS D_DonViTinhREFMua
	,'' soluogntext
	, SUM(cth.ChietKhauMua)/COUNT(cth.Id) AS ChietKhauMua
	, SUM(cth.SoLuongMua*cth.DonGiaMua*(100-cth.ChietKhauMua)/100)  AS ThanhTienMua
	, 0 AS Vat
	, '' AS AttachFile
	, ct.CreationTime
	, ISNULL((SELECT TOP (1) t.Username FROM [192.168.23.217].PMS.dbo.V_NhanVien_DangNhap t WHERE t.ID = ct.CreatorUserId ORDER BY t.ID),'') Created_By
	, ct.LastModificationTime
	, ISNULL((SELECT TOP (1) t.Username FROM [192.168.23.217].PMS.dbo.V_NhanVien_DangNhap t WHERE t.ID = ct.LastModifierUserId ORDER BY t.ID),'') AS LastModified_By
	, ct.IsDeleted
	, ISNULL(ct.ThanhTien,0) AS ThanhTienBanSauCK
	, ISNULL(ct.ChenhLech,0) AS ThanhTienLaiSauCK
	, 0 Statuss
	 FROM (
		SELECT dt.Id FROM [192.168.23.217].PMS.dbo.B_DuToan dt 
		WHERE 1=1 AND dt.TrangThai IN (2,3) -- 0: Nháp-- 1: Chờ duyệt-- 2: Phê duyệt-- 3: PHê duyệt BGĐ-- 4: Không phê duyệt-- 5: HỦy
		AND dt.IsDeleted = 0
	 )dt
	 INNER JOIN 
	 (
		SELECT ct.id, ct.B_DuToanREF, ct.PhanBoId, ct.ChenhLech, ct.ThanhTien,
		  ct.IsDeleted, ct.LastModifierUserId, ct.LastModificationTime, ct.CreatorUserId, ct.CreationTime
		FROM [192.168.23.217].PMS.dbo.B_DuToan_ChiTiet ct WHERE ct.IsDeleted = 0 AND  ISNULL(ct.PhanBoId,0) <> 0
		AND ct.LastModificationTime >= @NgayThucHien
	 )ct ON dt.Id = ct.B_DuToanREF
	 INNER JOIN 
	 (SELECT cth.IsDeleted, cth.id, cth.ThanhTienSauCK,cth.Vat, cth.PhaiTraNhaCungCap,
			 cth.ChietKhauMua, cth.DonGiaMua, cth.SoLuongMua, cth.D_DonViTinhREFMua,
			 cth.D_NhaCungCapREF, cth.KhoanMuc, cth.SoHopDongMua, cth.B_DuToan_ChiTiet_REF
			 FROM [192.168.23.217].PMS.dbo.B_DuToan_ChiTiet_HopDong cth WHERE 1=1  
		AND cth.IsDeleted = 0
	 )cth ON ct.Id = cth.B_DuToan_ChiTiet_REF
	 WHERE 1=1 
	 GROUP BY  ct.PhanBoId, ct.CreationTime, ct.CreatorUserId, ct.LastModificationTime
	, ct.LastModifierUserId, ct.IsDeleted, ct.ThanhTien , ct.ChenhLech 


	

	-- Set trang thai = 1 doi voi nhung truong hop sua chua 
	UPDATE #HopDongChiTiet_MuaNgoai_dev
		SET    [STATUS] = 1
		FROM  #HopDongChiTiet_MuaNgoai_dev t INNER JOIN HopDongChiTiet_MuaNgoai_dev  dc
		ON t.HopDongChiTietID = dc.HopDongChiTietID

	-- UPDATE GIA TRI CHO NHUNG BAN GHI DA TON TAI                                      
	   UPDATE DBO.HopDongChiTiet_MuaNgoai_dev
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
		FROM   #HopDongChiTiet_MuaNgoai_dev A 
		WHERE  [STATUS] = 1 AND A.HopDongChiTietID = HopDongChiTiet_MuaNgoai_dev.HopDongChiTietID
	-- INSERT ROW CHUA TON TAI
	INSERT INTO [dbo].HopDongChiTiet_MuaNgoai_dev
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
	FROM #HopDongChiTiet_MuaNgoai_dev   dchdct WHERE dchdct.[STATUS]=0

	UPDATE dbo.ThucChayMuaNgoaiChiTiet_dev
	SET ThanhTienLaiThucChaySauCK = CASE WHEN hdct.ThanhTienSauCKMua <> 0 THEN hdct.ThanhTienLaiSauCK*((mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)/hdct.ThanhTienSauCKMua)
									ELSE 0
									END
	FROM  dbo.ThucChayMuaNgoaiChiTiet_dev mn
	INNER JOIN #HopDongChiTiet_MuaNgoai_dev hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID

	UPDATE dbo.ThucChayMuaNgoaiChiTiet_dev
	SET ThanhTienThucChayBanSauCK = mn.ThanhTienLaiThucChaySauCK + (mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)
	FROM dbo.ThucChayMuaNgoaiChiTiet_dev mn
	INNER JOIN #HopDongChiTiet_MuaNgoai_dev hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID

	---------------------THUCCHAYMUANGOAICHITIET THUC CHAY MUA NGOAI------------------------------

	SET @NgayThucHien_ThucChayMN = 
	ISNULL((
			SELECT MAX(dchdct.LastModifiedAt)
			FROM   dbo.ThucChayMuaNgoaiChiTiet_dev dchdct
		),'2010-01-01')

	set @NgayThucHien_ThucChayMN = DATEADD(day,-1,@NgayThucHien_ThucChayMN)
	
	PRINT @NgayThucHien_ThucChayMN

	CREATE TABLE #ThucChayMuaNgoaiChiTiet_dev(
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

	
	INSERT INTO #ThucChayMuaNgoaiChiTiet_dev
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
	
	SELECT Id AS ThucChayMuaNgoaiChiTietID,
    HopDongId,
    PhanBoId,
    IIF(NgayBatDau = '0001-01-01','1900-01-01',NgayBatDau) AS NgayBatDau,
    IIF(NgayKetThuc = '0001-01-01','1900-01-01',NgayKetThuc) AS NgayKetThuc,
	CreationTime AS NgayThucChay,
	SoLuongChay,
	D_DonViTinhREF,
    ChietKhauMua,
    ISNULL(SoLuongChay,0)*ISNULL(DonGia,0) AS TienThucChay,
	0 AS ThanhTienThucChayBan,
	0 AS ThanhTienLaiThucChaySauCK,
    CreationTime,
    ISNULL((SELECT TOP (1) t.Username FROM [192.168.23.217].PMS.dbo.V_NhanVien_DangNhap t WHERE t.ID = CreatorUserId ORDER BY t.ID),'') AS Created_By,
    LastModificationTime,
    ISNULL((SELECT TOP (1) t.Username FROM [192.168.23.217].PMS.dbo.V_NhanVien_DangNhap t WHERE t.ID = LastModifierUserId ORDER BY t.ID),'') AS LastModified_By,
	TrangThai, --0 : mới,1: gửi duyệt;2 duyệt thanh toán
    IsDeleted,
	0 AS Statuss FROM [192.168.23.217].PMS.dbo.B_QuanLyThucChay
	WHERE LastModificationTime >= @NgayThucHien_ThucChayMN

	--DROP TABLE #HopDongChiTiet_MuaNgoai_dev
	-- Set trang thai = 1 doi voi nhung truong hop sua chua 
	UPDATE t
	SET t.[STATUS_MN] = 1
	, t.NgayThucChay = (CASE WHEN t.NgayThucChay = '1900-01-01' AND t.TuNgay <> '1900-01-01' THEN t.TuNgay
	WHEN t.NgayThucChay = '1900-01-01' AND t.TuNgay = '1900-01-01' THEN CONVERT(DATE,t.CreatedAt)
	ELSE CONVERT(DATE,t.CreatedAt)
	END)
	FROM  #ThucChayMuaNgoaiChiTiet_dev t INNER JOIN dbo.ThucChayMuaNgoaiChiTiet_dev  dc
	ON t.ThucChayMuaNgoaiChiTietID = dc.ThucChayMuaNgoaiChiTietID
		
	UPDATE #ThucChayMuaNgoaiChiTiet_dev
	SET ThanhTienLaiThucChaySauCK = CASE WHEN hdct.ThanhTienSauCKMua <> 0 THEN hdct.ThanhTienLaiSauCK*((mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)/hdct.ThanhTienSauCKMua)
									ELSE 0
									END
	FROM #ThucChayMuaNgoaiChiTiet_dev mn
	INNER JOIN dbo.HopDongChiTiet_MuaNgoai_dev hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID

	UPDATE #ThucChayMuaNgoaiChiTiet_dev
	SET ThanhTienThucChayBanSauCK = mn.ThanhTienLaiThucChaySauCK + (mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)
	FROM #ThucChayMuaNgoaiChiTiet_dev mn
	INNER JOIN dbo.HopDongChiTiet_MuaNgoai_dev hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID

	-- UPDATE GIA TRI CHO NHUNG BAN GHI DA TON TAI                                      

	UPDATE [dbo].[ThucChayMuaNgoaiChiTiet_dev]
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
 	FROM   #ThucChayMuaNgoaiChiTiet_dev A 
	WHERE  [STATUS_MN] = 1 AND A.[ThucChayMuaNgoaiChiTietID] = [ThucChayMuaNgoaiChiTiet_dev].ThucChayMuaNgoaiChiTietID


	--INSERT ROW CHUA TON TAI
	INSERT INTO [dbo].[ThucChayMuaNgoaiChiTiet_dev]
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
		0 TrangThaiTinhThucChay FROM #ThucChayMuaNgoaiChiTiet_dev
		WHERE [STATUS_MN] = 0

END



```
