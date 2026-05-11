# Stored Procedure: `Gen_InsertOrUpdate_ThucTreoHopDongChiTietTrinhDuyet_ChiTietLink`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-11-19 16:09:35.433000
- **Ngày sửa cuối**: 2019-05-13 09:33:47.610000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_ThucTreoHopDongChiTietTrinhDuyet_ChiTietLink]

*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucTreoHopDongChiTietTrinhDuyet_ChiTietLink] 	
As 	
BEGIN
	DECLARE @NgayThucHien DATETIME
	DECLARE @SQL NVARCHAR(MAX)
	
	SET @NgayThucHien = '2018-12-01'
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
	  NgayBatDau DATE DEFAULT NULL ,
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
	  NgayDuyet datetime DEFAULT NULL,
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
		  tchdct.NgayDuyet,
		  tchdct.Linkbai,
		  tchdct.Lst_NhanVienSoYeuLyLichREF,
		0 
	FROM OPENQUERY([MySQL],''CALL Abm_get_hdcn_confirm_thuctreo_chiphi_lnk_chitiet (''''' + CONVERT(NVARCHAR(50), @NgayThucHien, 120)
		+ ''''');'') tchdct'

	PRINT @SQL
	INSERT INTO #ThucTreoHopDongChiTietTrinhDuyet
	EXECUTE
	  (
		@SQL
	  )
	
	DELETE FROM ThucTreoHopDongChiTietTrinhDuyet_linkChitiet
	WHERE 1=1 

	INSERT INTO dbo.ThucTreoHopDongChiTietTrinhDuyet_linkChitiet
	SELECT *  FROM #ThucTreoHopDongChiTietTrinhDuyet

	DROP TABLE #ThucTreoHopDongChiTietTrinhDuyet
END


```
