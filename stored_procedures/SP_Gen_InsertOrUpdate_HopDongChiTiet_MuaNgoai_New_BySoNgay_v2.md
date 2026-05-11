# Stored Procedure: `Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_New_BySoNgay_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-11-01 10:00:23.383000
- **Ngày sửa cuối**: 2024-02-22 17:56:56.080000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
--exec [Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_New_BySoNgay_v0.1] 586259


CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_New_BySoNgay_v2]
	@HopDongChiTietID INT
As 	
BEGIN
    DECLARE @NgayThucHien DATETIME, @NgayThucHien_ThucChayMN DATETIME
	DECLARE @SQL NVARCHAR(MAX), @SQL_ThucChayMN NVARCHAR(MAX) = ''
	--SET @SoNgayLui = ISNULL(@SoNgayLui,0)

	SET @NgayThucHien = 
	ISNULL((
			SELECT MAX(dchdct.LastModifiedAt)
			FROM   DBO.HopDongChiTiet_MuaNgoai dchdct
		),'2010-01-01')

	--set @NgayThucHien = DATEADD(day,-@SoNgayLui,@NgayThucHien)

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
	, ISNULL((SELECT TOP (1) t.Username FROM ASDAG2.PMS.dbo.V_NhanVien_DangNhap t WHERE t.ID = ct.CreatorUserId ORDER BY t.ID),'') Created_By
	, (CASE WHEN CONVERT(DATE,dt.LastModificationTime) >= CONVERT(DATE,ct.LastModificationTime) THEN CONVERT(DATE,dt.LastModificationTime)
	 ELSE CONVERT(DATE,ct.LastModificationTime)
	 end) AS LastModificationTime
	, ISNULL((SELECT TOP (1) t.Username FROM ASDAG2.PMS.dbo.V_NhanVien_DangNhap t WHERE t.ID = ct.LastModifierUserId ORDER BY t.ID),'') AS LastModified_By
	, ct.IsDeleted
	, ISNULL(ct.ThanhTien,0) AS ThanhTienBanSauCK
	, ISNULL(ct.ChenhLech,0) AS ThanhTienLaiSauCK
	, 0 Statuss
	 FROM (
		SELECT dt.Id, dt.LastModificationTime FROM ASDAG2.PMS.dbo.B_DuToan dt 
		WHERE 1=1 AND dt.TrangThai IN (2,3) -- 0: Nháp-- 1: Chờ duyệt-- 2: Phê duyệt-- 3: PHê duyệt BGĐ-- 4: Không phê duyệt-- 5: HỦy
		AND dt.IsDeleted = 0
	 )dt
	 INNER JOIN 
	 (
		SELECT ct.id, ct.B_DuToanREF, ct.PhanBoId, ct.ChenhLech, ct.ThanhTien,
		  ct.IsDeleted, ct.LastModifierUserId, ct.LastModificationTime, ct.CreatorUserId, ct.CreationTime
		FROM ASDAG2.PMS.dbo.B_DuToan_ChiTiet ct WHERE ct.IsDeleted = 0 AND  ISNULL(ct.PhanBoId,0) <> 0
		--AND ct.LastModificationTime >= @NgayThucHien
	 )ct ON dt.Id = ct.B_DuToanREF
	 INNER JOIN 
	 (SELECT cth.IsDeleted, cth.id, cth.ThanhTienSauCK,cth.Vat, cth.PhaiTraNhaCungCap,
			 cth.ChietKhauMua, cth.DonGiaMua, cth.SoLuongMua, cth.D_DonViTinhREFMua,
			 cth.D_NhaCungCapREF, cth.KhoanMuc, cth.SoHopDongMua, cth.B_DuToan_ChiTiet_REF
			 FROM ASDAG2.PMS.dbo.B_DuToan_ChiTiet_HopDong cth WHERE 1=1  
		AND cth.IsDeleted = 0
	 )cth ON ct.Id = cth.B_DuToan_ChiTiet_REF
	 WHERE 1=1 
	 --AND (CASE WHEN CONVERT(DATE,dt.LastModificationTime) >= CONVERT(DATE,ct.LastModificationTime) THEN CONVERT(DATE,dt.LastModificationTime)
	 --ELSE CONVERT(DATE,ct.LastModificationTime)
	 --end) >= @NgayThucHien
	 AND ct.PhanBoId = @HopDongChiTietID
	 GROUP BY  ct.PhanBoId, ct.CreationTime, ct.CreatorUserId, ct.LastModificationTime, dt.LastModificationTime
	, ct.LastModifierUserId, ct.IsDeleted, ct.ThanhTien , ct.ChenhLech 

	--SELECT * FROM #HopDongChiTiet_MuaNgoai
	

	-- Set trang thai = 1 doi voi nhung truong hop sua chua 
		UPDATE t
		SET t.STATUS = 1
		FROM  #HopDongChiTiet_MuaNgoai t INNER JOIN dbo.HopDongChiTiet_MuaNgoai  dc
		ON t.HopDongChiTietID = dc.HopDongChiTietID
		WHERE 1=1 and t.HopDongChiTietID = @HopDongChiTietID


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
		WHERE A.STATUS = 1 and A.HopDongChiTietID = @HopDongChiTietID
	
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
	FROM #HopDongChiTiet_MuaNgoai   dchdct WHERE dchdct.[STATUS]=0 and dchdct.HopDongChiTietID = @HopDongChiTietID

	UPDATE mn
	SET mn.ThanhTienLaiThucChaySauCK = CASE WHEN hdct.ThanhTienSauCKMua <> 0 THEN hdct.ThanhTienLaiSauCK*((mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)/hdct.ThanhTienSauCKMua)
									ELSE 0
									END
	FROM  dbo.ThucChayMuaNgoaiChiTiet mn
	INNER JOIN #HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE 1=1 and hdct.HopDongChiTietID = @HopDongChiTietID

	UPDATE mn
	SET mn.ThanhTienThucChayBanSauCK = mn.ThanhTienLaiThucChaySauCK + (mn.ThanhTienMuaNgoaiTruocCK*(100-mn.ChietKhauMuaNgoai)/100)
	FROM dbo.ThucChayMuaNgoaiChiTiet mn
	INNER JOIN #HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE 1=1 and hdct.HopDongChiTietID = @HopDongChiTietID
	END

```
