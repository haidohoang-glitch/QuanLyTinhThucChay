# Stored Procedure: `Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_New_v1_asd14`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-08-31 10:52:19.047000
- **Ngày sửa cuối**: 2021-08-31 10:52:19.047000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_New_v1_asd14]
*/
create PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_New_v1_asd14]
As 	
BEGIN
    DECLARE @NgayThucHien DATETIME, @NgayThucHien_ThucChayMN DATETIME
	DECLARE @SQL NVARCHAR(MAX), @SQL_ThucChayMN NVARCHAR(MAX) = ''

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

	INSERT INTO #HopDongChiTiet_MuaNgoai
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
	, ISNULL((SELECT TOP (1) t.Username FROM asd14.PMS.dbo.V_NhanVien_DangNhap t WHERE t.ID = ct.CreatorUserId ORDER BY t.ID),'') Created_By
	, (CASE WHEN CONVERT(DATE,dt.LastModificationTime) >= CONVERT(DATE,ct.LastModificationTime) THEN CONVERT(DATE,dt.LastModificationTime)
	 ELSE CONVERT(DATE,ct.LastModificationTime)
	 end) AS LastModificationTime
	, ISNULL((SELECT TOP (1) t.Username FROM asd14.PMS.dbo.V_NhanVien_DangNhap t WHERE t.ID = ct.LastModifierUserId ORDER BY t.ID),'') AS LastModified_By
	, ct.IsDeleted
	, ISNULL(ct.ThanhTien,0) AS ThanhTienBanSauCK
	, ISNULL(ct.ChenhLech,0) AS ThanhTienLaiSauCK
	, 0 Statuss
	 FROM (
		SELECT dt.Id, dt.LastModificationTime FROM asd14.PMS.dbo.B_DuToan dt 
		WHERE 1=1 AND dt.TrangThai IN (2,3) -- 0: Nháp-- 1: Chờ duyệt-- 2: Phê duyệt-- 3: PHê duyệt BGĐ-- 4: Không phê duyệt-- 5: HỦy
		AND dt.IsDeleted = 0
	 )dt
	 INNER JOIN 
	 (
		SELECT ct.id, ct.B_DuToanREF, ct.PhanBoId, ct.ChenhLech, ct.ThanhTien,
		  ct.IsDeleted, ct.LastModifierUserId, ct.LastModificationTime, ct.CreatorUserId, ct.CreationTime
		FROM asd14.PMS.dbo.B_DuToan_ChiTiet ct WHERE 1=1 -- ct.IsDeleted = 0 
		AND  ISNULL(ct.PhanBoId,0) <> 0
		--AND ct.LastModificationTime >= @NgayThucHien
	 )ct ON dt.Id = ct.B_DuToanREF
	 INNER JOIN 
	 (SELECT cth.IsDeleted, cth.id, cth.ThanhTienSauCK,cth.Vat, cth.PhaiTraNhaCungCap,
			 cth.ChietKhauMua, cth.DonGiaMua, cth.SoLuongMua, cth.D_DonViTinhREFMua,
			 cth.D_NhaCungCapREF, cth.KhoanMuc, cth.SoHopDongMua, cth.B_DuToan_ChiTiet_REF
			 FROM asd14.PMS.dbo.B_DuToan_ChiTiet_HopDong cth WHERE 1=1  
		AND cth.IsDeleted = 0
	 )cth ON ct.Id = cth.B_DuToan_ChiTiet_REF
	 WHERE 1=1 
	 AND (CASE WHEN CONVERT(DATE,dt.LastModificationTime) >= CONVERT(DATE,ct.LastModificationTime) THEN CONVERT(DATE,dt.LastModificationTime)
	 ELSE CONVERT(DATE,ct.LastModificationTime)
	 end) >= @NgayThucHien
	 GROUP BY  ct.PhanBoId, ct.CreationTime, ct.CreatorUserId, ct.LastModificationTime, dt.LastModificationTime
	, ct.LastModifierUserId, ct.IsDeleted, ct.ThanhTien , ct.ChenhLech 


	

	-- Set trang thai = 1 doi voi nhung truong hop sua chua 
		UPDATE t
		SET t.STATUS = 1
		FROM  #HopDongChiTiet_MuaNgoai t INNER JOIN dbo.HopDongChiTiet_MuaNgoai  dc
		ON t.HopDongChiTietID = dc.HopDongChiTietID
		WHERE 1=1


	-- UPDATE GIA TRI CHO NHUNG BAN GHI DA TON TAI  
	                                       
	   UPDATE dt
		SET
			dt.HopDongChiTietID = A.HopDongChiTietID,
			dt.SoHopDongMua = A.SoHopDongMua,
			dt.DonGiaMua = A.DonGiaMua,
			dt.SoLuongMua = A.SoLuongMua,
			dt.DonViTinh = A.DonViTinh,
			dt.SoLuongText = A.SoLuongText,
			dt.ChietKhauMua = A.ChietKhauMua,
			dt.ThanhTienSauCKMua = A.ThanhTienSauCKMua,
			dt.VAT = A.VAT,
			dt.AttachFile = A.AttachFile,
			dt.CreatedAt = A.CreatedAt,
			dt.CreatedBy = A.CreatedBy,
			dt.LastModifiedAt = A.LastModifiedAt,
			dt.LastModifiedBy = A.LastModifiedBy,
			dt.DeletedStatus = A.DeletedStatus,
			dt.ThanhTienBanSauCK = A.ThanhTienBanSauCK,
			dt.ThanhTienLaiSauCK = A.ThanhTienLaiSauCK
		FROM   #HopDongChiTiet_MuaNgoai A 
		INNER JOIN dbo.HopDongChiTiet_MuaNgoai dt ON A.HopDongChiTietID = dt.HopDongChiTietID
		WHERE A.STATUS = 1
	
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

	UPDATE mn
	SET mn.ThanhTienLaiThucChaySauCK = CASE WHEN hdct.ThanhTienSauCKMua <> 0 THEN hdct.ThanhTienLaiSauCK*((mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)/hdct.ThanhTienSauCKMua)
									ELSE 0
									END
	FROM  dbo.ThucChayMuaNgoaiChiTiet mn
	INNER JOIN #HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE 1=1

	UPDATE mn
	SET mn.ThanhTienThucChayBanSauCK = mn.ThanhTienLaiThucChaySauCK + (mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)
	FROM dbo.ThucChayMuaNgoaiChiTiet mn
	INNER JOIN #HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE 1=1

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
		[NgayDuyet] [Datetime] NULL,
		[NguoiDuyet] [Nvarchar](100),
		[NgayChot] [Datetime] NULL,
		[NguoiChot] [Nvarchar](100),
		[STATUS_MN] INT
	)

	
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
		[NgayDuyet],
		[NguoiDuyet],
		[NgayChot],
		[NguoiChot],
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
    ISNULL((SELECT TOP (1) t.Username FROM asd14.PMS.dbo.V_NhanVien_DangNhap t WHERE t.ID = CreatorUserId ORDER BY t.ID),'') AS Created_By,
    LastModificationTime,
    ISNULL((SELECT TOP (1) t.Username FROM asd14.PMS.dbo.V_NhanVien_DangNhap t WHERE t.ID = LastModifierUserId ORDER BY t.ID),'') AS LastModified_By,
	TrangThai, --0 : mới,1: gửi duyệt;2 duyệt thanh toán, 3 -- gửi duyệt thực chạy, --4 duyệt thực chạy
    IsDeleted,
	NgayDuyet,
	ISNULL((SELECT TOP (1) t.tendangnhap FROM asd14.PMS.[dbo].[V_NguoiDung] t WHERE t.OxUserID = NguoiDuyet ORDER BY t.OxUserID),'') AS NguoiDuyet,
	NgayChot,
	ISNULL((SELECT TOP (1) t.tendangnhap FROM asd14.PMS.[dbo].[V_NguoiDung] t WHERE t.OxUserID = NguoiChot ORDER BY t.OxUserID),'') AS NguoiChot,
	0 AS Statuss FROM asd14.PMS.dbo.B_QuanLyThucChay
	WHERE LastModificationTime >= @NgayThucHien_ThucChayMN

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
	WHERE 1=1
		
	UPDATE mn
	SET mn.ThanhTienLaiThucChaySauCK = CASE WHEN hdct.ThanhTienSauCKMua <> 0 THEN hdct.ThanhTienLaiSauCK*((mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)/hdct.ThanhTienSauCKMua)
									ELSE 0
									END
	FROM #ThucChayMuaNgoaiChiTiet mn
	INNER JOIN dbo.HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE 1=1

	UPDATE mn
	SET mn.ThanhTienThucChayBanSauCK = mn.ThanhTienLaiThucChaySauCK + (mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)
	FROM #ThucChayMuaNgoaiChiTiet mn
	INNER JOIN dbo.HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE 1=1

	-- UPDATE GIA TRI CHO NHUNG BAN GHI DA TON TAI                                      

	UPDATE tc
	SET tc.[ThucChayMuaNgoaiChiTietID] = A.ThucChayMuaNgoaiChiTietID
      ,tc.[HopDongREF] = A.HopDongREF
      ,tc.[HopDongChiTietREF] = A.HopDongChiTietREF
      ,tc.[TuNgay] = A.TuNgay
      ,tc.[DenNgay] = A.DenNgay
      ,tc.[NgayThucChay] = A.NgayThucChay
      ,tc.[SoLuongThucChay] = A.SoLuongThucChay
      ,tc.[DmDonViTinhREF] = A.DmDonViTinhREF
      ,tc.[ChietKhauMuaNgoai] = A.ChietKhauMuaNgoai
      ,tc.[ThanhTienMuaNgoaiTruocCK] = A.ThanhTienMuaNgoaiTruocCK
      ,tc.[ThanhTienThucChayBanSauCK] = A.ThanhTienThucChayBanSauCK
      ,tc.[ThanhTienLaiThucChaySauCK] = A.ThanhTienLaiThucChaySauCK
      ,tc.[CreatedAt] = A.CreatedAt
      ,tc.[CreatedBy] = A.CreatedBy
      ,tc.[LastModifiedAt] = A.LastModifiedAt
      ,tc.[LastModifiedBy] = A.LastModifiedBy
	  ,tc.[Status]  = A.Status_approved
      ,tc.[DeletedStatus] = A.DeletedStatus
	  ,tc.[NgayDuyet] = A.NgayDuyet
	  ,tc.[NguoiDuyet] = A.NguoiDuyet
	  ,tc.[NgayChot] = A.NgayChot
	  ,tc.[NguoiChot] = A.NguoiChot
 	FROM   #ThucChayMuaNgoaiChiTiet A 
	INNER JOIN  [dbo].[ThucChayMuaNgoaiChiTiet] tc
	ON A.[ThucChayMuaNgoaiChiTietID] = tc.ThucChayMuaNgoaiChiTietID
	WHERE  A.[STATUS_MN] = 1


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
		   ,[NgayDuyet]
		   ,[NguoiDuyet]
		   ,[NgayChot]
		   ,[NguoiChot]
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
		NgayDuyet,
		NguoiDuyet,
		NgayChot,
		NguoiChot,
		0 TrangThaiTinhThucChay FROM #ThucChayMuaNgoaiChiTiet
		WHERE [STATUS_MN] = 0

END



```
