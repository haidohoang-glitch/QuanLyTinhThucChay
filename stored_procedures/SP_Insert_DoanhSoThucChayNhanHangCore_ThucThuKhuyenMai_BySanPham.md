# Stored Procedure: `Insert_DoanhSoThucChayNhanHangCore_ThucThuKhuyenMai_BySanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-09-26 16:00:09.737000
- **Ngày sửa cuối**: 2016-09-26 16:00:09.737000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [Insert_DoanhSoThucChayNhanHangCore_ThucThuKhuyenMai_BySanPham] '2013-09-09'

CREATE  PROCEDURE [dbo].[Insert_DoanhSoThucChayNhanHangCore_ThucThuKhuyenMai_BySanPham] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @Result BIGINT, @SoHopDong NVARCHAR(50),@HopDongFK INT,@HopDongChiTietID INT
	DECLARE @TenSanPham NVARCHAR(100), @DmSanPhamREF INT, @LstDmNhanHangREF NVARCHAR(200) 
    DECLARE @DoanhSoThucChay BIGINT 
    DECLARE @DmNhanHangREF INT, @TenNhanHang NVARCHAR(200), @SoluongHDCT INT, @SoLuongNhan INT
    DECLARE @TongThanhTienSP BIGINT, @TiLeDoanhSoKy FLOAT, @v_count_checkthucchay INT
    DECLARE @DsNganhHangREF NVARCHAR(50), @TenNhanVien NVARCHAR(300), @DmNhanVienREF INT
    DECLARE @DsTenNganhHang NVARCHAR(200),@DmKhachHangREF INT,@TenKhachHang NVARCHAR(400)
    
    SET @DsTenNganhHang = ''
    SET @Result = 0
    SET @SoluongHDCT = 1
    SET @v_count_checkthucchay = 0
    SET @DsNganhHangREF = ''
    
	DECLARE Record_Cursor1 CURSOR FOR 
	SELECT DISTINCT tcdt.SoHopDong, tcdt.HopDongID, a.TenNhanVien, a.SysNhanVienREF, tcdt.TenSanPham, tcdt.DmSanPhamREF,a.DmKhachHangREF,a.TenKhachHang
	  FROM
	(
		SELECT distinct hd.SoHopDong, hd.HopDongID,hdct.HopDongChiTietID, hd.TenNhanVien, hd.SysNhanVienREF , hdct.TenSanPham, hdct.DmSanPhamREF,hd.DmKhachHangREF,hd.TenKhachHang
		FROM hopdong hd 
		INNER JOIN	HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	)a
	RIGHT JOIN 
	(
		SELECT DISTINCT A.SoHopDong,A.HopDongID, A.HopDongChiTietREF, A.DmSanPhamREF, A.TenSanPham FROM
		(
			SELECT DISTINCT tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.TenNhanVien, tcdt.SysNhanVienREF
			  FROM ThucChayDaTinh tcdt
			WHERE 1 = 1
			AND (
				tcdt.DmSanPhamREF NOT IN (299,337,299,144,585,628) 
				AND NOT(tcdt.DmSanPhamREF = 375 AND YEAR(tcdt.NgayThucHien) = 2013)
			)
			AND tcdt.HopDongChiTietREF = 0
			AND tcdt.HopDongID<> 0
			AND tcdt.TrangThaiHopDong <> 3
			AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF,@NgayThucHien) =0
			AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
			UNION
			SELECT DISTINCT tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.TenNhanVien, tcdt.SysNhanVienREF
			  FROM ThucChayDaTinhAdmarket tcdt
			WHERE 1 = 1
			AND tcdt.DmSanPhamREF IN (299,337,299,144,585,375,628)
			AND tcdt.HopDongChiTietREF = 0
			AND tcdt.HopDongID<> 0
			AND tcdt.TrangThaiHopDong <> 3
			AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF,@NgayThucHien) =0
			AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
 
		)A
	) tcdt ON tcdt.HopDongID = a.HopDongID AND a.HopDongChiTietID = tcdt.HopDongChiTietREF
	--WHERE tcdt.HopDongID=16714
	 
	OPEN Record_Cursor1
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @TenNhanVien, @DmNhanVienREF, @TenSanPham, @DmSanPhamREF ,@DmKhachHangREF ,@TenKhachHang 
	WHILE @@FETCH_STATUS = 0
	BEGIN
		--Check hop dong, san pham co thuc chay ngay
		BEGIN
			SET @DmNhanHangREF = 0
			SET @TenNhanHang = ''
			SET @LstDmNhanHangREF = (SELECT
			stuff(
			(
			SELECT DISTINCT cast(',' as varchar(max)) + U.DanhSachNhanHangREF
			from HopDongChiTiet U
			WHERE U.HopDongFK = @HopDongFK
			AND U.DmSanPhamREF = @DmSanPhamREF
			AND U.DeletedStatus = 0--CHO NAY CAN XEM LAI
			for xml path('') 
			), 1, 1, '') AS DanhSachNhanHang
			)
			--PRINT @LstDmNhanHangREF
			--Check HopDong co hopdongchitiet = 0 ?
			SELECT @SoLuongNhan = count(a.DmNhanHang) from
			(
				SELECT distinct dbo.FormatString(item) DmNhanHang
				FROM dbo.ArrayToTable(dbo.Array(@LstDmNhanHangREF,','))
			)a
			IF(@SoLuongNhan > 0)
			BEGIN
				DECLARE Record_Cursor2 CURSOR FOR
					SELECT distinct dbo.FormatString(item) DmNhanHang
					FROM dbo.ArrayToTable(dbo.Array(@LstDmNhanHangREF,','))
				OPEN Record_Cursor2 
				FETCH NEXT FROM Record_Cursor2 INTO @DmNhanHangREF
				WHILE @@FETCH_STATUS = 0
				BEGIN
					set @DoanhSoThucChay = 0
					SELECT @TenNhanHang = dnh.TenNhanHang, @DsNganhHangREF = dnh.DmNghanhHangREF
					  FROM DmNhanHang dnh
					WHERE dnh.DmNhanHangID = @DmNhanHangREF
					SET @TenNhanHang = ISNULL(@TenNhanHang,'')
					SET @DsNganhHangREF = ISNULL(@DsNganhHangREF,'')
					
					--INSERT DU LIEU DOANHSOTHUCCHAYNHANHANGCORE
					PRINT @HopDongFK print @DmNhanHangREF
					INSERT INTO DoanhSoThucChayNhanHangCore
					SELECT A.NgayThucHien,A.DmNhanHangREF,A.TenNhanHang,A.DsNganhHangREF,A.DsTenNganhHang,
						   A.HopDongID,A.SoHopDong,A.TenNhanVien,A.SysNhanVienREF,A.HopDongChiTietREF,
						   A.TenSanPham,A.DmSanPhamREF,A.TenWebsite,A.DmWebsiteREF,
						   0 ThucThuPhatSinhDauKy,
						   SUM(A.ThucThuPhatSinhTrongKy) * dbo.fn_TiLeNhanHangTheoHopDong(@HopDongFK,@DmNhanHangREF,@HopDongChiTietID) ThucThuPhatSinhTrongKy,
						   0 ThucThuPhatSinhCuoiKy,
						  
						   SUM(A.KhuyenMaiPhatSinhTrongKy) KhuyenMaiPhatSinhTrongKy,
						   0 KhuyenMaiPhatSinhDauKy,
						   0 KhuyenMaiPhatSinhCuoiKy,
						   0 NoiBoPhatSinhDauKy,
						   0 NoiBoPhatSinhTrongKy,
						   0 NoiBoPhatSinhCuoiKy,
						   
						   0 SoLuongPhatSinhDauKy,
						   SUM(A.SoLuongPhatSinhTrongKy)*dbo.fn_TiLeNhanHangTheoHopDong(@HopDongFK,@DmNhanHangREF,@HopDongChiTietID) SoLuongPhatSinhTrongKy,
						   0 SoLuongPhatSinhCuoiKy,
							
						   0 SoLuongKhuyenMaiPhatSinhDauKy,
						   SUM(A.SoLuongKMPhatSinh) SoLuongKhuyenMaiPhatSinhTrongKy,
						   0 SoLuongKhuyenMaiPhatSinhCuoiKy,
							
						   0 SoLuongNoiBoPhatSinhDauKy,
						   0 SoLuongNoiBoPhatSinhTrongKy,
						   0 SoLuongNoiBoPhatSinhCuoiKy,
						   
						   '' DienGiai,
						   'ASD' CreatedBy,
						   GETDATE() CreatedAt,
						   'ASD' LastModifiedBy,
						   GETDATE() LastModifiedAt,
						   0 DeletedStatus,
						   0 PrintStatus,
						   0 RecordStatus,
						   A.TenDangNhap,
						   A.DmPhongBanREF,
						   A.DmBoPhanREF,
						   A.DmNhomLamViecREF,
						   A.Nam,
						   A.Quy,
						   A.Thang
						   ,A.NgayDanhSoHopDong
						   ,A.DmDiaDiemLamViecREF
							,A.TenDiaDiemLamViec
							,@DmKhachHangREF DmKhachHangREF
							,@TenKhachHang TenKhachHang
						FROM   (
								   SELECT @NgayThucHien NgayThucHien,
										  @DmNhanHangREF DmNhanHangREF,
										  @TenNhanHang TenNhanHang,
										  @DsNganhHangREF DsNganhHangREF,
										  @DsTenNganhHang DsTenNganhHang,
										  tcdt.HopDongID,
										  tcdt.SoHopDong,
										  tcdt.TenNhanVien,
										  tcdt.SysNhanVienREF,
										  0 HopDongChiTietREF,
										  tcdt.TenSanPham,
										  tcdt.DmSanPhamREF,
										  tcdt.TenWebsite,
										  tcdt.DmWebsiteREF,
										  tcdt.TenDangNhap,
										  tcdt.DmPhongBanREF,
										  tcdt.DmBoPhanREF,
										  tcdt.DmNhomLamViecREF,
										  YEAR(@NgayThucHien) Nam,
										  MONTH(@NgayThucHien) Thang,
										  DATEPART(QQ,@NgayThucHien) Quy,
										  0 AS ThucThuPhatSinhDauKy,
										  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS 
										  ThucThuPhatSinhTrongKy,
										  0 AS ThucThuPhatSinhCuoiKy,
										  0 AS KhuyenMaiPhatSinhDauKy,
										  SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) 
										  AS KhuyenMaiPhatSinhTrongKy,
										  0 AS KhuyenMaiPhatSinhCuoiKy,
										  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS SoLuongPhatSinhTrongKy,
										  SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi) AS SoLuongKMPhatSinh
										  ,tcdt.DmDiaDiemLamViecREF
											,tcdt.TenDiaDiemLamViec
											,tcdt.NgayDanhSoHopDong
								   FROM   ThucChayDaTinh tcdt
								   WHERE  tcdt.HopDongID = @HopDongFK
										  AND tcdt.HopDongChiTietREF = 0
										  AND tcdt.DmSanPhamREF = @DmSanPhamREF
										  AND CONVERT(date, tcdt.NgayThucHien) = @NgayThucHien
								   GROUP BY tcdt.HopDongID,tcdt.SoHopDong,tcdt.TenNhanVien,tcdt.SysNhanVienREF,
										  tcdt.TenSanPham,tcdt.DmSanPhamREF,tcdt.TenWebsite,tcdt.DmWebsiteREF,
										  tcdt.TenDangNhap,
										  tcdt.DmPhongBanREF,
										  tcdt.DmBoPhanREF,
										  tcdt.DmNhomLamViecREF
										  ,tcdt.DmDiaDiemLamViecREF
											,tcdt.TenDiaDiemLamViec
											,tcdt.NgayDanhSoHopDong
								   UNION
								   SELECT @NgayThucHien NgayThucHien,
										  @DmNhanHangREF DmNhanHangREF,
										  @TenNhanHang TenNhanHang,
										  @DsNganhHangREF DsNganhHangREF,
										  @DsTenNganhHang DsTenNganhHang,
										  tcdt.HopDongID,
										  tcdt.SoHopDong,
										  tcdt.TenNhanVien,
										  tcdt.SysNhanVienREF,
										  0 HopDongChiTietREF,
										  tcdt.TenSanPham,
										  tcdt.DmSanPhamREF,
										  tcdt.TenWebsite,
										  tcdt.DmWebsiteREF,
										  tcdt.TenDangNhap,
										  tcdt.DmPhongBanREF,
										  tcdt.DmBoPhanREF,
										  tcdt.DmNhomLamViecREF,
										  YEAR(@NgayThucHien) Nam,
										  MONTH(@NgayThucHien) Thang,
										  DATEPART(QQ,@NgayThucHien) Quy,
										  0 AS ThucThuPhatSinhDauKy,
										  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS 
										  ThucThuPhatSinhTrongKy,
										  0 AS ThucThuPhatSinhCuoiKy,
										  0 KhuyenMaiPhatSinhDauKy,
										  SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS KhuyenMaiPhatSinhTrongKy,
										  0 KhuyenMaiPhatSinhCuoiKy,
										  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS SoLuongPhatSinhTrongKy,
										  SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi) AS SoLuongKMPhatSinh
										  ,tcdt.DmDiaDiemLamViecREF
											,tcdt.TenDiaDiemLamViec
											,tcdt.NgayDanhSoHopDong
								   FROM   ThucChayDaTinhAdmarket tcdt
								   WHERE  tcdt.HopDongID = @HopDongFK
								   AND tcdt.HopDongChiTietREF = 0
										  AND tcdt.DmSanPhamREF = @DmSanPhamREF
										  AND CONVERT(date, tcdt.NgayThucHien) = @NgayThucHien
								   GROUP BY tcdt.HopDongID,tcdt.SoHopDong,tcdt.TenNhanVien,tcdt.SysNhanVienREF,
										  tcdt.TenSanPham,tcdt.DmSanPhamREF,tcdt.TenWebsite,tcdt.DmWebsiteREF,
										  tcdt.TenDangNhap,
										  tcdt.DmPhongBanREF,
										  tcdt.DmBoPhanREF,
										  tcdt.DmNhomLamViecREF
										  ,tcdt.DmDiaDiemLamViecREF
										  ,tcdt.TenDiaDiemLamViec
										  ,tcdt.NgayDanhSoHopDong
							   )A
							   WHERE (ROUND(A.ThucThuPhatSinhTrongKy,0) <> 0 OR ROUND(A.KhuyenMaiPhatSinhTrongKy,0) <> 0)
						GROUP BY  A.NgayThucHien,A.DmNhanHangREF,A.TenNhanHang,A.DsNganhHangREF,A.DsTenNganhHang,A.HopDongID,A.SoHopDong,
							   A.TenNhanVien,A.SysNhanVienREF,A.HopDongChiTietREF,A.TenSanPham,A.DmSanPhamREF,A.TenWebsite,A.DmWebsiteREF,
							   A.TenDangNhap,
							   A.DmPhongBanREF,
							   A.DmBoPhanREF,
							   A.DmNhomLamViecREF,
							   A.Nam,
							   A.Quy,
							   A.Thang
							   ,A.DmDiaDiemLamViecREF
							   ,A.TenDiaDiemLamViec
							   ,A.NgayDanhSoHopDong
					FETCH NEXT FROM Record_Cursor2 INTO @DmNhanHangREF
				END
				CLOSE Record_Cursor2
				DEALLOCATE Record_Cursor2
			END
			ELSE
				BEGIN
					INSERT INTO DoanhSoThucChayNhanHangCore
					SELECT A.NgayThucHien,A.DmNhanHangREF,A.TenNhanHang,A.DsNganhHangREF,A.DsTenNganhHang,
						   A.HopDongID,A.SoHopDong,A.TenNhanVien,A.SysNhanVienREF,A.HopDongChiTietREF,
						   A.TenSanPham,A.DmSanPhamREF,A.TenWebsite,A.DmWebsiteREF,
						   0 ThucThuPhatSinhDauKy,
						   SUM(A.ThucThuPhatSinhTrongKy)ThucThuPhatSinhTrongKy,
						   0 ThucThuPhatSinhCuoiKy,
						   0 KhuyenMaiPhatSinhDauKy,
						   SUM(A.KhuyenMaiPhatSinhTrongKy) KhuyenMaiPhatSinhTrongKy,
						   0 KhuyenMaiPhatSinhCuoiKy,
						   0 NoiBoPhatSinhDauKy,
						   0 NoiBoPhatSinhTrongKy,
						   0 NoiBoPhatSinhCuoiKy,
						   
						   0 SoLuongPhatSinhDauKy,
						   SUM(A.SoLuongPhatSinhTrongKy) SoLuongPhatSinhTrongKy,
						   0 SoLuongPhatSinhCuoiKy,
							
						   0 SoLuongKhuyenMaiPhatSinhDauKy,
						   SUM(A.SoLuongKMPhatSinh) SoLuongKhuyenMaiPhatSinhTrongKy,
						   0 SoLuongKhuyenMaiPhatSinhCuoiKy,
							
						   0 SoLuongNoiBoPhatSinhDauKy,
						   0 SoLuongNoiBoPhatSinhTrongKy,
						   0 SoLuongNoiBoPhatSinhCuoiKy,
						   
						   '' DienGiai,
						   'ASD' CreatedBy,
						   GETDATE() CreatedAt,
						   'ASD' LastModifiedBy,
						   GETDATE() LastModifiedAt,
						   0 DeletedStatus,
						   0 PrintStatus,
						   0 RecordStatus,
						   A.TenDangNhap,
						   A.DmPhongBanREF,
						   A.DmBoPhanREF,
						   A.DmNhomLamViecREF,
						   A.Nam,
						   A.Quy,
						   A.Thang
						   ,A.NgayDanhSoHopDong
						   ,A.DmDiaDiemLamViecREF
							,A.TenDiaDiemLamViec
							,@DmKhachHangREF DmKhachHangREF
							,@TenKhachHang TenKhachHang
					FROM   (
							   SELECT @NgayThucHien NgayThucHien,
									  @DmNhanHangREF DmNhanHangREF,
									  @TenNhanHang TenNhanHang,
									  @DsNganhHangREF DsNganhHangREF,
									  @DsTenNganhHang DsTenNganhHang,
									  tcdt.HopDongID,
									  tcdt.SoHopDong,
									  tcdt.TenNhanVien,
									  tcdt.SysNhanVienREF,
									  0 HopDongChiTietREF,
									  tcdt.TenSanPham,
									  tcdt.DmSanPhamREF,
									  tcdt.TenWebsite,
									  tcdt.DmWebsiteREF,
									  tcdt.TenDangNhap,
									  tcdt.DmPhongBanREF,
									  tcdt.DmBoPhanREF,
									  tcdt.DmNhomLamViecREF,
									  YEAR(@NgayThucHien) Nam,
									  MONTH(@NgayThucHien) Thang,
									  DATEPART(QQ,@NgayThucHien) Quy,
									  0 AS ThucThuPhatSinhDauKy,
									  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS 
									  ThucThuPhatSinhTrongKy,
									  0 AS ThucThuPhatSinhCuoiKy,
									  0 KhuyenMaiPhatSinhDauKy,
									  SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS KhuyenMaiPhatSinhTrongKy,
									  0 KhuyenMaiPhatSinhCuoiKy,
									  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS SoLuongPhatSinhTrongKy,
									  SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi) AS SoLuongKMPhatSinh
									  ,tcdt.DmDiaDiemLamViecREF
									  ,tcdt.TenDiaDiemLamViec
									  ,tcdt.NgayDanhSoHopDong
							   FROM   ThucChayDaTinh tcdt
							   WHERE  tcdt.HopDongID = @HopDongFK
							         AND tcdt.HopDongChiTietREF = 0
									  AND tcdt.DmSanPhamREF = @DmSanPhamREF
									  AND CONVERT(date, tcdt.NgayThucHien) = @NgayThucHien
							   GROUP BY tcdt.HopDongID,tcdt.SoHopDong,tcdt.TenNhanVien,tcdt.SysNhanVienREF,
									  tcdt.TenSanPham,tcdt.DmSanPhamREF,tcdt.TenWebsite,tcdt.DmWebsiteREF,
									  tcdt.TenDangNhap,
									  tcdt.DmPhongBanREF,
									  tcdt.DmBoPhanREF,
									  tcdt.DmNhomLamViecREF
									  ,tcdt.DmDiaDiemLamViecREF
									,tcdt.TenDiaDiemLamViec 
									,tcdt.NgayDanhSoHopDong
							   UNION
							   SELECT @NgayThucHien NgayThucHien,
									  @DmNhanHangREF DmNhanHangREF,
									  @TenNhanHang TenNhanHang,
									  @DsNganhHangREF DsNganhHangREF,
									  @DsTenNganhHang DsTenNganhHang,
									  tcdt.HopDongID,
									  tcdt.SoHopDong,
									  tcdt.TenNhanVien,
									  tcdt.SysNhanVienREF,
									  0 HopDongChiTietREF,
									  tcdt.TenSanPham,
									  tcdt.DmSanPhamREF,
									  tcdt.TenWebsite,
									  tcdt.DmWebsiteREF,
									  tcdt.TenDangNhap,
									  tcdt.DmPhongBanREF,
									  tcdt.DmBoPhanREF,
									  tcdt.DmNhomLamViecREF,
									  YEAR(@NgayThucHien) Nam,
									  MONTH(@NgayThucHien) Thang,
									  DATEPART(QQ,@NgayThucHien) Quy,
									   0 AS ThucThuPhatSinhDauKy,
									  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS 
									  ThucThuPhatSinhTrongKy,
									  0 AS ThucThuPhatSinhCuoiKy,
									  0 KhuyenMaiPhatSinhDauKy,
									  SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS KhuyenMaiPhatSinhTrongKy,
									  0 KhuyenMaiPhatSinhCuoiKy,
									  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS SoLuongPhatSinhTrongKy,
									  SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi) AS SoLuongKMPhatSinh
									  ,tcdt.DmDiaDiemLamViecREF
									  ,tcdt.TenDiaDiemLamViec
									  ,tcdt.NgayDanhSoHopDong
							   FROM   ThucChayDaTinhAdmarket tcdt
							   WHERE  tcdt.HopDongID = @HopDongFK
							      AND tcdt.HopDongChiTietREF = 0
									  AND tcdt.DmSanPhamREF = @DmSanPhamREF
									  AND CONVERT(date, tcdt.NgayThucHien) = @NgayThucHien
							   GROUP BY tcdt.HopDongID,tcdt.SoHopDong,tcdt.TenNhanVien,tcdt.SysNhanVienREF,
									  tcdt.TenSanPham,tcdt.DmSanPhamREF,tcdt.TenWebsite,tcdt.DmWebsiteREF,
									  tcdt.TenDangNhap,
									  tcdt.DmPhongBanREF,
									  tcdt.DmBoPhanREF,
									  tcdt.DmNhomLamViecREF
									  ,tcdt.DmDiaDiemLamViecREF
									,tcdt.TenDiaDiemLamViec
									,tcdt.NgayDanhSoHopDong
						   )A
						   WHERE (ROUND(A.ThucThuPhatSinhTrongKy,0) <>0 OR round(A.KhuyenMaiPhatSinhTrongKy,0)<> 0)
					GROUP BY  A.NgayThucHien,A.DmNhanHangREF,A.TenNhanHang,A.DsNganhHangREF,A.DsTenNganhHang,A.HopDongID,A.SoHopDong,
						   A.TenNhanVien,A.SysNhanVienREF,A.HopDongChiTietREF,A.TenSanPham,A.DmSanPhamREF,A.TenWebsite,A.DmWebsiteREF,
						   A.TenDangNhap,
						   A.DmPhongBanREF,
						   A.DmBoPhanREF,
						   A.DmNhomLamViecREF,
						   A.Nam,
						   A.Quy,
						   A.Thang
						   ,A.DmDiaDiemLamViecREF
							,A.TenDiaDiemLamViec
							,A.NgayDanhSoHopDong
				END
		END
		FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @TenNhanVien, @DmNhanVienREF, @TenSanPham, @DmSanPhamREF ,@DmKhachHangREF ,@TenKhachHang 
	END
	
	CLOSE Record_Cursor1
	DEALLOCATE Record_Cursor1
	--SELECT '1'
END

--EXEC [Insert_DoanhSoThucChayCoreNhanHang_ThucThu] '2013-12-31'

```
