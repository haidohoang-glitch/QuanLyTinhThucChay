# Stored Procedure: `Syn_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_fromSQLServer`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-13 15:21:13.520000
- **Ngày sửa cuối**: 2020-09-22 16:03:06.423000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Syn_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_fromSQLServer] 

*/
CREATE PROCEDURE [dbo].[Syn_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_fromSQLServer] 	
As 	
BEGIN
	DECLARE @NgayThucHien DATETIME, @NgayThucHienXoa DATETIME
	DECLARE @SQL NVARCHAR(MAX)
	SET @NgayThucHien = 
		ISNULL((
			SELECT MAX(dchdct.LastModifiedAt)
			FROM   dbo.ThucTreoHopDongChiTietTrinhDuyet_ThucTreo dchdct
		),'2017-01-01')

	SET @NgayThucHien = '2018-01-01'
	SET @NgayThucHienXoa = DATEADD(HOUR,-24,@NgayThucHien)
	--SET @NgayThucHien = '2018-01-01'

	--CHO NAY PHAI XOA VI KHONG TIM THAY JOB NAO DA DONG BO DU LIEU VE TABLE LAM DOUBLE DU LIEU
	DELETE FROM  dbo.ThucTreoHopDongChiTietTrinhDuyet_ThucTreo
	WHERE LastModifiedAt >= @NgayThucHienXoa

	PRINT @NgayThucHien

	CREATE TABLE #ThucTreoHopDongChiTietTrinhDuyet_Thuctreo (
	  ThucTreoHopDongChiTietTrinhDuyetID INT NOT NULL ,
	  HopDongREF INT NOT NULL,
	  HopDongChiTietREF INT NOT NULL,
	  DmHinhThucQuangCaoREF INT NOT NULL ,
	  DmSanPhamREF INT NOT NULL ,
	  TenNhanHang NVARCHAR(300) DEFAULT NULL ,
	  NhanHangREF INT NOT NULL DEFAULT '0',
	  DmWebsiteREF int DEFAULT NULL,
	  TenWebsite NVARCHAR(255) DEFAULT NULL,
	  Soluong DECIMAL DEFAULT NULL ,
	  DmDonViTinhREF INT DEFAULT NULL,
	  DonViTinh NVARCHAR(50) DEFAULT NULL,
	  DonGia decimal(10,0) DEFAULT NULL,
	  ChietKhau float DEFAULT NULL,
	  TongTien float DEFAULT NULL ,
	  NgayBatDau date DEFAULT NULL ,
	  NgayKetThuc date DEFAULT NULL ,
	  TrangThai smallint DEFAULT NULL ,--'trang thai: 0 = luu nhap, 1 = trinh duyet, 2 = da duyet, 3 = tu choi',
	  IsLocked smallint NOT NULL DEFAULT '0',
	  CreatedAt datetime DEFAULT NULL,
	  CreatedBy NVARCHAR(50) DEFAULT NULL,
	  LastModifiedAt datetime DEFAULT NULL,
	  LastModifiedBy NVARCHAR(50) DEFAULT NULL,
	  SubmittedAt datetime DEFAULT NULL,
	  SubmittedBy NVARCHAR(50) DEFAULT NULL,
	  ApprovedAt datetime DEFAULT NULL,
	  ApprovedBy NVARCHAR(50) DEFAULT NULL,
	  Note NVARCHAR(500) DEFAULT NULL,
	  ThucChayHopDongChiTietREF INT NOT NULL DEFAULT '0',
	  DeletedStatus smallint NOT NULL DEFAULT '0',
	  Linkbai NVARCHAR(MAX),
	  Lst_NhanVienSoYeuLyLichREF NVARCHAR(100),
	  record_status SMALLINT
	) 

	
		INSERT INTO #ThucTreoHopDongChiTietTrinhDuyet_Thuctreo
		(
		    ThucTreoHopDongChiTietTrinhDuyetID,
		    HopDongREF,
		    HopDongChiTietREF,
		    DmHinhThucQuangCaoREF,
		    DmSanPhamREF,
		    TenNhanHang,
		    NhanHangREF,
		    DmWebsiteREF,
		    TenWebsite,
		    Soluong,
		    DmDonViTinhREF,
		    DonViTinh,
		    DonGia,
		    ChietKhau,
		    TongTien,
		    NgayBatDau,
		    NgayKetThuc,
		    TrangThai,
		    IsLocked,
		    CreatedAt,
		    CreatedBy,
		    LastModifiedAt,
		    LastModifiedBy,
		    SubmittedAt,
		    SubmittedBy,
		    ApprovedAt,
		    ApprovedBy,
		    Note,
		    ThucChayHopDongChiTietREF,
		    DeletedStatus,
		    Linkbai,
		    Lst_NhanVienSoYeuLyLichREF,
		    record_status
		)
		
		
		SELECT tc.Id AS ThucTreoHopDongChiTietTrinhDuyetID,
               tc.Contract_Id AS HopDongREF,
               tc.Contract_Detail_Id AS HopDongChiTietREF,
               tc.Product_Formality_Id AS  DmHinhThucQuangCaoREF,
               tc.Product_Id AS DmSanPhamREF,
               tc.Brand_Name AS TenNhanHang,
               tc.Brand_Id AS NhanHangREF,
               tc.Website_Id AS DmWebsiteREF,
               tc.Website_Name AS TenWebsite,
               tc.Quantity AS Soluong,
               tc.UnitId AS DmDonViTinhREF,
               tc.UnitName AS DonViTinh,
               tc.UnitPrice AS DonGia,
               tc.Discount AS ChietKhau,
               tc.TotalMoney AS TongTien,
               tc.StartDate AS NgayBatDau,
               tc.EndDate AS NgayKetThuc,
               tc.RecordStatus AS TrangThai,
               tc.IsLocked AS IsLocked,
               tc.CreatedAt,
               tc.CreatedBy,
               tc.LastModifiedAt,
               tc.LastModifiedBy,
               tc.SubmittedAt,
               tc.SubmittedBy,
               tc.ApprovedAt,
               tc.ApprovedBy,
               tc.Note,
               tc.SyncId,
               tc.DeletedStatus,
			   '' AS linkBai,
			   (select top (1) tca.NhanVien_Id from  [192.168.23.150].ThucTreo.dbo.[ThucTreo_ChiPhi_Account] tca where tca.thuctreo_chiphi_REF = tc.id and tca.deleted_status = 0) AS ListNhanVienREF,
               0 status_table FROM [192.168.23.150].ThucTreo.dbo.ThucTreo_ChiPhi tc
		WHERE tc.LastModifiedAt >= @NgayThucHien

		UPDATE t
		SET    t.record_status = 1
		FROM  #ThucTreoHopDongChiTietTrinhDuyet_Thuctreo t INNER JOIN dbo.ThucTreoHopDongChiTietTrinhDuyet_ThucTreo dc
		ON t.ThucTreoHopDongChiTietTrinhDuyetID = dc.ThucTreoHopDongChiTietTrinhDuyetID
	-- Update nhung row da ton ton                                      


	UPDATE B
	 SET B.[HopDongREF] =A.HopDongREF
      ,B.[HopDongChiTietREF] = A.HopDongChiTietREF
      ,B.[DmHinhThucQuangCaoREF] = A.DmHinhThucQuangCaoREF
      ,B.[DmSanPhamREF] = A.DmSanPhamREF
      ,B.[TenNhanHang] = A.TenNhanHang
      ,B.[NhanHangREF] = A.NhanHangREF
      ,B.[DmWebsiteREF] = A.DmWebsiteREF
      ,B.[TenWebsite] = A.TenWebsite
      ,B.[Soluong] = A.Soluong
      ,B.[DmDonViTinhREF] = A.DmDonViTinhREF
      ,B.[DonViTinh] = A.DonViTinh
      ,B.[DonGia] = A.DonGia
      ,B.[ChietKhau] = A.ChietKhau
      ,B.[TongTien] = A.TongTien
      ,B.[NgayBatDau] = A.NgayBatDau
      ,B.[NgayKetThuc] = A.NgayKetThuc
      ,B.[TrangThai] = A.TrangThai
      ,B.[IsLocked] = A.IsLocked
      ,B.[CreatedAt] = A.CreatedAt
      ,B.[CreatedBy] = A.CreatedBy
      ,B.[LastModifiedAt] = A.LastModifiedAt
      ,B.[LastModifiedBy] = A.LastModifiedBy
      ,B.[SubmittedAt] = A.SubmittedAt
      ,B.[SubmittedBy] = A.SubmittedBy
      ,B.[ApprovedAt] = A.ApprovedAt
      ,B.[ApprovedBy] = A.ApprovedBy
      ,B.[Note] = A.Note
      ,B.[ThucChayHopDongChiTietREF] = A.ThucChayHopDongChiTietREF
      ,B.[DeletedStatus] = A.DeletedStatus
      ,B.[Linkbai] = A.Linkbai
	  ,B.[Lst_NhanVienSoYeuLyLichREF] = ISNULL(A.Lst_NhanVienSoYeuLyLichREF,'')
	FROM  [dbo].ThucTreoHopDongChiTietTrinhDuyet_ThucTreo B INNER JOIN #ThucTreoHopDongChiTietTrinhDuyet_Thuctreo A 
	ON B.ThucTreoHopDongChiTietTrinhDuyetID = A.ThucTreoHopDongChiTietTrinhDuyetID
	WHERE  A.record_status = 1 

	-- Insert Row chua ton tai
	INSERT INTO [dbo].ThucTreoHopDongChiTietTrinhDuyet_ThucTreo
	(
	    ThucTreoHopDongChiTietTrinhDuyetID,
	    HopDongREF,
	    HopDongChiTietREF,
	    DmHinhThucQuangCaoREF,
	    DmSanPhamREF,
	    TenNhanHang,
	    NhanHangREF,
	    DmWebsiteREF,
	    TenWebsite,
	    Soluong,
	    DmDonViTinhREF,
	    DonViTinh,
	    DonGia,
	    ChietKhau,
	    TongTien,
	    NgayBatDau,
	    NgayKetThuc,
	    TrangThai,
	    IsLocked,
	    CreatedAt,
	    CreatedBy,
	    LastModifiedAt,
	    LastModifiedBy,
	    SubmittedAt,
	    SubmittedBy,
	    ApprovedAt,
	    ApprovedBy,
	    Note,
	    ThucChayHopDongChiTietREF,
	    DeletedStatus,
	    Linkbai,
	    Lst_NhanVienSoYeuLyLichREF
	)
	
		SELECT dchdct.ThucTreoHopDongChiTietTrinhDuyetID
           ,dchdct.HopDongREF
           ,dchdct.HopDongChiTietREF
           ,dchdct.DmHinhThucQuangCaoREF
           ,dchdct.DmSanPhamREF
           ,dchdct.TenNhanHang
           ,dchdct.NhanHangREF
           ,dchdct.DmWebsiteREF
           ,dchdct.TenWebsite
           ,dchdct.Soluong
           ,dchdct.DmDonViTinhREF
           ,dchdct.DonViTinh
           ,dchdct.DonGia
           ,dchdct.ChietKhau
           ,dchdct.TongTien
           ,dchdct.NgayBatDau
           ,dchdct.NgayKetThuc
           ,dchdct.TrangThai
           ,dchdct.IsLocked
           ,dchdct.CreatedAt
           ,dchdct.CreatedBy
           ,dchdct.LastModifiedAt
           ,dchdct.LastModifiedBy
           ,dchdct.SubmittedAt
           ,dchdct.SubmittedBy
           ,dchdct.ApprovedAt
           ,dchdct.ApprovedBy
           ,dchdct.Note
           ,dchdct.ThucChayHopDongChiTietREF
           ,dchdct.DeletedStatus
           ,dchdct.Linkbai
		   ,ISNULL(dchdct.Lst_NhanVienSoYeuLyLichREF,'')
	FROM #ThucTreoHopDongChiTietTrinhDuyet_Thuctreo dchdct WHERE dchdct.record_status=0

	DROP TABLE #ThucTreoHopDongChiTietTrinhDuyet_Thuctreo
	
END
```
