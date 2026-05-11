# Stored Procedure: `ThucChay_InsertThongTinHopDongInventory`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-12-30 10:48:46.483000
- **Ngày sửa cuối**: 2022-06-13 17:44:57.960000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
/*
[dbo].[ThucChay_InsertThongTinHopDongInventory] '2021-05-26'
	
*/

-------------------------------------------------------------
CREATE PROCEDURE [dbo].[ThucChay_InsertThongTinHopDongInventory] 
	@NgayThucHien DATETIME
AS
BEGIN
	CREATE TABLE #DmThongTinHopDongBanInventory (
	[HopDongREF] [int] NOT NULL,
	[SoHopDong] [nvarchar](100) NOT NULL,
	[NgayDanhSo] [datetime] NOT NULL,
	[DmNhanVienREF] [int] NOT NULL,
	[DmKhachHangREF] [int] NOT NULL,
	[HopDongChiTietREF] [int] NULL,
	[DmSanPhamREF] [int] NULL,
	[TenSanPham] [nvarchar](200) NULL,
	[GhiChu] [nvarchar](300) NULL,
	[CreatedAt] [datetime] NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[LastModifiedAt] [datetime] NULL,
	[LastModifiedBy] [nvarchar](50) NULL,
	[RecordStatus] [int] NULL,
	[DeletedStatus] [int] NULL,
	[Status] INT
	) 

	INSERT INTO #DmThongTinHopDongBanInventory
	        ( HopDongREF ,
	          SoHopDong ,
	          NgayDanhSo ,
	          DmNhanVienREF ,
	          DmKhachHangREF ,
	          HopDongChiTietREF ,
	          DmSanPhamREF ,
	          TenSanPham ,
	          GhiChu ,
	          CreatedAt ,
	          CreatedBy ,
	          LastModifiedAt ,
	          LastModifiedBy ,
	          RecordStatus ,
	          DeletedStatus,
			  [Status]
	        )
		SELECT hd.HopDongID, hd.SoHopDong, hd.NgayDanhSoHopDong
		, hd.SysNhanVienREF, hd.DmKhachHangREF
		, 0 HopDongChiTietREF, 0 DmSanPhamREF, '' TenSanPham 
		, '' GhiChu, GETDATE() CreatedAt, 'ASD' CreatedBy
		, GETDATE() LastModifiedAt, 'ASD' LastModifiedBy
		, 0 RecordStatus
		, 0 DeletedStatus 
		, 0 [status]
		FROM dbo.HopDong hd
		WHERE hd.TrangThaiHopDong <> 3
		AND hd.DeletedStatus = 0
		AND (hd.DmKhachHangREF IN (6546,10272,8581,9988,9938) --DANH SACH CÁC KHACH HANG ADMICRO BAN INVENTORY
			OR EXISTS(SELECT TOP (1) hdct.HopDongFK FROM dbo.HopDongChiTiet hdct
			WHERE hdct.HopDongFK = hd.HopDongID
			AND hdct.DeletedStatus = 0
			AND hdct.DmLoaiREF = 42
			AND hdct.DmLoaiNenTangREF = 9 
			AND hdct.DmSanPhamREF NOT IN( 733 ,817) --loai bo dmsanpham Nhieu san pham, marketing fee
			ORDER BY hdct.HopDongFK)
		)
		AND (CONVERT(DATE,hd.LastModifiedAt) = @NgayThucHien
			OR EXISTS(SELECT TOP (1) hdct.HopDongFK FROM dbo.HopDongChiTiet hdct
			WHERE hdct.HopDongFK = hd.HopDongID
			AND hdct.DeletedStatus = 0
			AND hdct.DmLoaiREF = 42
			AND hdct.DmLoaiNenTangREF = 9 
			AND hdct.DmSanPhamREF NOT IN( 733 ,817) --loai bo dmsanpham Nhieu san pham, marketing fee
			AND CONVERT(DATE,hdct.LastModifiedAt) = @NgayThucHien
			ORDER BY hdct.HopDongFK)
		)
		
		--THEM THONG TIN HOP DONG CO PHAN BO VOI NEN TAN LA: --Khong tin cho TH co nen tang la: 9-	Direct Tag, Admatic
		
		--select * from #DmThongTinHopDongBanInventory

		IF(EXISTS(SELECT TOP (1) HopDongREF FROM #DmThongTinHopDongBanInventory ORDER BY HopDongREF))
		BEGIN
			--Xac dinh trang thai nhung hop dong da ton tai trong DmThongTinHopDongBanInventory
			UPDATE iv
			SET iv.[Status] =1
			FROM #DmThongTinHopDongBanInventory iv 
			INNER JOIN dbo.DmThongTinHopDongBanInventory v
			ON iv.HopDongREF = v.HopDongREF

			INSERT INTO dbo.DmThongTinHopDongBanInventory
			        ( HopDongREF ,
			          SoHopDong ,
			          NgayDanhSo ,
			          DmNhanVienREF ,
			          DmKhachHangREF ,
			          HopDongChiTietREF ,
			          DmSanPhamREF ,
			          TenSanPham ,
			          GhiChu ,
			          CreatedAt ,
			          CreatedBy ,
			          LastModifiedAt ,
			          LastModifiedBy ,
			          RecordStatus ,
			          DeletedStatus
			        )
			SELECT HopDongREF ,
			          SoHopDong ,
			          NgayDanhSo ,
			          DmNhanVienREF ,
			          DmKhachHangREF ,
			          HopDongChiTietREF ,
			          DmSanPhamREF ,
			          TenSanPham ,
			          GhiChu ,
			          CreatedAt ,
			          CreatedBy ,
			          LastModifiedAt ,
			          LastModifiedBy ,
			          RecordStatus ,
			          DeletedStatus 
			FROM #DmThongTinHopDongBanInventory t
			WHERE t.[Status] = 0
		END
		DROP TABLE #DmThongTinHopDongBanInventory
	SELECT '1'
END


```
