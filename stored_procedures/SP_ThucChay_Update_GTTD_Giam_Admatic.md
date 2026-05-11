# Stored Procedure: `ThucChay_Update_GTTD_Giam_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-09 17:10:38.083000
- **Ngày sửa cuối**: 2017-02-09 17:10:38.083000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongFK` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@TongGiaTriGiam` | `float(8)` | No |
| `@TiLeGiam` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_Update_GTTD_Giam_Admatic] 47330, 106061,100000,0.000034567, '2016-12-11'
CREATE  PROCEDURE [dbo].[ThucChay_Update_GTTD_Giam_Admatic] 
	@HopDongFK INT,
	@HopDongChiTietID INT,
	@TongGiaTriGiam FLOAT,
	@TiLeGiam FLOAT,
	@NgayThucHien DATETIME

	--SELECT * FROM hopdongchitiet WHERE hopdongchitietid = 106061
AS
BEGIN
	DECLARE @DmSanPhamREF INT, @TenSanPham NVARCHAR(300), @ThanhTienThucChay FLOAT=0, @GiaTriThucChayGiam_SanPham FLOAT=0
	DECLARE @ThucChayDaTinhID NVARCHAR(500),@ThanhTienThucChay_Recod FLOAT =0, @SoLuongThucChay_Record INT
	, @DonGiaTheoDVT FLOAT
	DECLARE @GiaTriThucChayGiam FLOAT=0, @SoLuongThucChayGiam INT=0
	DECLARE @v_count INT = 0
	

	DECLARE Cursor_hdct_sanpham CURSOR FOR
		--1. XAC DINH GIA TRI GIAM TREN TUNG SAN PHAM, THUC HIEN GIAM DEU TREN TUNG SAN PHAM VA THUC HIEN QUAY NGUOC
	SELECT A.*
	, (CONVERT(FLOAT,A.ThanhtienthucChay) * @TiLeGiam) GiaTriThucChayGiam
	FROM
	(
		SELECT DmSanPhamREF, TenSanPham
		, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhtienthucChay
		FROM dbo.ThucChayDaTinh
		WHERE DmHinhThucQuangCao = 42
		AND HopDongChiTietREF = @HopDongChiTietID
		AND HopDongID = @HopDongFK
		AND NgayThucHien < @NgayThucHien
		GROUP BY HopDongChiTietREF, DmSanPhamREF, TenSanPham
	)A

	OPEN Cursor_hdct_sanpham
	FETCH NEXT FROM Cursor_hdct_sanpham INTO @DmSanPhamREF, @TenSanPham, @ThanhTienThucChay, @GiaTriThucChayGiam_SanPham
	WHILE @@FETCH_STATUS =0
	BEGIN
		PRINT 'XAC DINH BAN GHI GIAM GIA GIA TRI'
		PRINT @TenSanPham + ' ,GIA TRI THUCCHAY GIAM:' + CONVERT(NVARCHAR(50),@GiaTriThucChayGiam_SanPham)

		SET @v_count = 0
		---------
		DECLARE Cursor_hdct_sanpham_record CURSOR FOR
		--1. XAC DINH GIA TRI GIAM TREN TUNG SAN PHAM
		SELECT ThucChayDaTinhID, (ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) ThanhTienThucChay
		, (SoLuongThucChay + SoLuongThayDoi) SoLuongThucChayGiam
		, DonGiaTheoDonVi
		FROM dbo.ThucChayDaTinh
		WHERE DmHinhThucQuangCao = 42
		AND HopDongChiTietREF = @HopDongChiTietID
		AND HopDongID = @HopDongFK
		AND DmSanPhamREF = @DmSanPhamREF
		ORDER BY DmSanPhamREF,NgayThucHien DESC, CreatedAt DESC
		
		OPEN Cursor_hdct_sanpham_record
		FETCH NEXT FROM Cursor_hdct_sanpham_record INTO @ThucChayDaTinhID, @ThanhTienThucChay_Recod
		, @SoLuongThucChay_Record, @DonGiaTheoDVT
		WHILE @@FETCH_STATUS =0
		BEGIN
			IF(@DonGiaTheoDVT = 0)
			SET @DonGiaTheoDVT = 1
			PRINT CONVERT(NVARCHAR(50),@GiaTriThucChayGiam_SanPham)
			PRINT CONVERT(NVARCHAR(50),@ThanhTienThucChay_Recod)

			--PRINT 'CHECK VA CAP NHAT THONG TIN GIA TRI THAY DOI'
			PRINT''
			IF(@ThanhTienThucChay_Recod <> 0)
			BEGIN
				IF(@GiaTriThucChayGiam_SanPham > @ThanhTienThucChay_Recod)
				BEGIN
					SET @GiaTriThucChayGiam_SanPham = @GiaTriThucChayGiam_SanPham - @ThanhTienThucChay_Recod
					SET @GiaTriThucChayGiam = @ThanhTienThucChay_Recod
					SET @SoLuongThucChayGiam = @SoLuongThucChay_Record
				END
				ELSE
				BEGIN
					SET @GiaTriThucChayGiam =  @GiaTriThucChayGiam_SanPham
					SET @SoLuongThucChayGiam = @GiaTriThucChayGiam/@DonGiaTheoDVT
					SET @GiaTriThucChayGiam_SanPham = 0
				END
			END
			ELSE
			BEGIN
				SET @GiaTriThucChayGiam = 0
				SET @SoLuongThucChayGiam = 0
			END
			PRINT CONVERT(NVARCHAR(50),@GiaTriThucChayGiam_SanPham)

			EXEC [ThucChay_Insert_GTTD_Giam_ThucChayDaTinh_Admatic] 
					@ThucChayDaTinhID ,--@ThucChayDaTinhID NVARCHAR(500),
					@NgayThucHien, --@NgayThucHien DATETIME,
					@HopDongFK, --@HopDongID INT, 
					@HopDongChiTietID, --@HopDongChiTietID INT,
					@DmSanPhamREF, --@DmSanPhamREF INT,
					@GiaTriThucChayGiam, --@GiaTriThucChayGiam FLOAT,
					@SoLuongThucChayGiam, --@SoLuongThucChayGiam INT,
					0, --@GiaTriThucChayKM FLOAT,
					0 --@SoLuongThucChayKMGiam INT
			
			IF (@GiaTriThucChayGiam_SanPham = 0)
				BREAK --THOAT KHOI VONG Cursor_hdct_sanpham_record
		FETCH NEXT FROM Cursor_hdct_sanpham_record INTO @ThucChayDaTinhID, @ThanhTienThucChay_Recod
		, @SoLuongThucChay_Record, @DonGiaTheoDVT
		END
		CLOSE Cursor_hdct_sanpham_record;
		DEALLOCATE Cursor_hdct_sanpham_record;
		---------
	FETCH NEXT FROM Cursor_hdct_sanpham INTO @DmSanPhamREF, @TenSanPham, @ThanhTienThucChay, @GiaTriThucChayGiam_SanPham
	END
	CLOSE Cursor_hdct_sanpham;
	DEALLOCATE Cursor_hdct_sanpham;
	
END

```
