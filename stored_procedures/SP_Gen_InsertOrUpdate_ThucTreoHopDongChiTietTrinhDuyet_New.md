# Stored Procedure: `Gen_InsertOrUpdate_ThucTreoHopDongChiTietTrinhDuyet_New`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-08-17 10:07:45.620000
- **Ngày sửa cuối**: 2018-11-08 17:45:57.750000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_ThucTreoHopDongChiTietTrinhDuyet_New]

*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucTreoHopDongChiTietTrinhDuyet_New] 	
As 	
BEGIN
	DECLARE @NgayThucHien DATETIME
	DECLARE @SQL NVARCHAR(MAX)
	SET @NgayThucHien = 
		ISNULL((
			SELECT MAX(dchdct.LastModifiedAt)
			FROM   ThucTreoHopDongChiTietTrinhDuyet dchdct
		),'2017-01-01')

	SET @NgayThucHien = DATEADD(HOUR,-8,@NgayThucHien)

	--SET @NgayThucHien = '2018-01-01'
	PRINT @NgayThucHien

	CREATE TABLE #ThucTreoHopDongChiTietTrinhDuyet (
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

	SET @SQL = 
		'
	 SELECT 
		 tchdct.Id AS ThucTreoHopDongChiTietTrinhDuyet,
		  tchdct.ContractId AS HopDongREF,
		  tchdct.ContractDetailId AS HopDongChiTietREF,
		  tchdct.ProductFormalityId AS DmHinhThucQuangCaoREF,
		  tchdct.ProductId AS DmSanPhamREF,
		  tchdct.BrandName AS TenNhanHang,
		  tchdct.BrandId AS NhanHangREF,
		  tchdct.WebsiteId AS DmWebsiteREF,
		  tchdct.WebsiteName AS TenWebsite,
		  tchdct.Quantity AS SoLuong,
		  tchdct.UnitId AS DmDonViTinhREF,
		  tchdct.UnitName AS DonViTinh,
		  tchdct.UnitPrice AS DonGia,
		  tchdct.Discount AS ChietKhau,
		  tchdct.TotalMoney AS TongTien,
		  tchdct.StartDate AS NgayBatDau,
		  tchdct.EndDate AS NgayKetThuc,
		  tchdct.RecordStatus AS TrangThai,
		  tchdct.IsLocked,
		  tchdct.CreatedAt,
		  tchdct.CreatedBy,
		  tchdct.LastModifiedAt,
		  tchdct.LastModifiedBy,
		  tchdct.SubmittedAt,
		  tchdct.SubmittedBy,
		  tchdct.ApprovedAt,
		  tchdct.ApprovedBy,
		  tchdct.Note,
		  tchdct.SyncId AS ThucChayHopDongChiTietREF,
		  tchdct.DeletedStatus,
		  tchdct.Linkbai,
		  tchdct.Lst_NhanVienSoYeuLyLichREF,
		0
	FROM OPENQUERY([MySQL],''CALL Abm_get_hdcn_confirm_thuctreo_chiphi (''''' + CONVERT(NVARCHAR(50), @NgayThucHien, 120)
		+ ''''');'') tchdct'

	PRINT @SQL
	INSERT INTO #ThucTreoHopDongChiTietTrinhDuyet
	EXECUTE
	  (
		@SQL
	  )
	--SELECT * FROM #DmSanPham
	   -- Set trang thai = 1 doi voi nhung truong hop sua chua 
		--SET @NhanHang =  [dbo].[ReplaceNhanHangDoubleNhay](@NhanHang)
		UPDATE #ThucTreoHopDongChiTietTrinhDuyet 
		SET    record_status = 1
		FROM  #ThucTreoHopDongChiTietTrinhDuyet t INNER JOIN ThucTreoHopDongChiTietTrinhDuyet dc
		ON t.ThucTreoHopDongChiTietTrinhDuyetID = dc.ThucTreoHopDongChiTietTrinhDuyetID
	-- Update nhung row da ton ton                                      

	UPDATE [dbo].[ThucTreoHopDongChiTietTrinhDuyet]
	 SET [HopDongREF] =A.HopDongREF
      ,[HopDongChiTietREF] = A.HopDongChiTietREF
      ,[DmHinhThucQuangCaoREF] = A.DmHinhThucQuangCaoREF
      ,[DmSanPhamREF] = A.DmSanPhamREF
      ,[TenNhanHang] = A.TenNhanHang
      ,[NhanHangREF] = A.NhanHangREF
      ,[DmWebsiteREF] = A.DmWebsiteREF
      ,[TenWebsite] = A.TenWebsite
      ,[Soluong] = A.Soluong
      ,[DmDonViTinhREF] = A.DmDonViTinhREF
      ,[DonViTinh] = A.DonViTinh
      ,[DonGia] = A.DonGia
      ,[ChietKhau] = A.ChietKhau
      ,[TongTien] = A.TongTien
      ,[NgayBatDau] = A.NgayBatDau
      ,[NgayKetThuc] = A.NgayKetThuc
      ,[TrangThai] = A.TrangThai
      ,[IsLocked] = A.IsLocked
      ,[CreatedAt] = A.CreatedAt
      ,[CreatedBy] = A.CreatedBy
      ,[LastModifiedAt] = A.LastModifiedAt
      ,[LastModifiedBy] = A.LastModifiedBy
      ,[SubmittedAt] = A.SubmittedAt
      ,[SubmittedBy] = A.SubmittedBy
      ,[ApprovedAt] = A.ApprovedAt
      ,[ApprovedBy] = A.ApprovedBy
      ,[Note] = A.Note
      ,[ThucChayHopDongChiTietREF] = A.ThucChayHopDongChiTietREF
      ,[DeletedStatus] = A.DeletedStatus
      ,[Linkbai] = A.Linkbai
	  ,[Lst_NhanVienSoYeuLyLichREF] = ISNULL(A.Lst_NhanVienSoYeuLyLichREF,'')
	FROM   #ThucTreoHopDongChiTietTrinhDuyet A 
	WHERE  record_status = 1 AND A.ThucTreoHopDongChiTietTrinhDuyetID=[dbo].[ThucTreoHopDongChiTietTrinhDuyet].ThucTreoHopDongChiTietTrinhDuyetID
	-- Insert Row chua ton tai
	INSERT INTO [dbo].[ThucTreoHopDongChiTietTrinhDuyet]
           ([ThucTreoHopDongChiTietTrinhDuyetid]
           ,[HopDongREF]
           ,[HopDongChiTietREF]
           ,[DmHinhThucQuangCaoREF]
           ,[DmSanPhamREF]
           ,[TenNhanHang]
           ,[NhanHangREF]
           ,[DmWebsiteREF]
           ,[TenWebsite]
           ,[Soluong]
           ,[DmDonViTinhREF]
           ,[DonViTinh]
           ,[DonGia]
           ,[ChietKhau]
           ,[TongTien]
           ,[NgayBatDau]
           ,[NgayKetThuc]
           ,[TrangThai]
           ,[IsLocked]
           ,[CreatedAt]
           ,[CreatedBy]
           ,[LastModifiedAt]
           ,[LastModifiedBy]
           ,[SubmittedAt]
           ,[SubmittedBy]
           ,[ApprovedAt]
           ,[ApprovedBy]
           ,[Note]
           ,[ThucChayHopDongChiTietREF]
           ,[DeletedStatus]
           ,[Linkbai]
		   ,[Lst_NhanVienSoYeuLyLichREF])
 

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
	FROM #ThucTreoHopDongChiTietTrinhDuyet dchdct WHERE dchdct.record_status=0

	DROP TABLE #ThucTreoHopDongChiTietTrinhDuyet
END
```
