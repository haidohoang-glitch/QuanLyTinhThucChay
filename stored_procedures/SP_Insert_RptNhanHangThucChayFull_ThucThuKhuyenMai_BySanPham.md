# Stored Procedure: `Insert_RptNhanHangThucChayFull_ThucThuKhuyenMai_BySanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-02-12 10:39:58.193000
- **Ngày sửa cuối**: 2015-02-12 10:43:55.010000

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

--EXEC [Insert_DoanhSoThucChayNhanHangCore_ThucThu_BySanPham] '2013-01-01'

CREATE  PROCEDURE [dbo].[Insert_RptNhanHangThucChayFull_ThucThuKhuyenMai_BySanPham] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @Result BIGINT, @SoHopDong NVARCHAR(50),@HopDongFK INT,@HopDongChiTietID INT
	DECLARE @TenSanPham NVARCHAR(100), @DmSanPhamREF INT, @LstDmNhanHangREF NVARCHAR(200) 
    DECLARE @DoanhSoThucChay BIGINT 
    DECLARE @DmNhanHangREF INT, @TenNhanHang NVARCHAR(200), @SoluongHDCT INT, @SoLuongNhan INT
    DECLARE @TongThanhTienSP BIGINT, @TiLeDoanhSoKy FLOAT, @v_count_checkthucchay INT
    DECLARE @DsNganhHangREF NVARCHAR(50), @TenNhanVien NVARCHAR(300), @DmNhanVienREF INT
    DECLARE @DsTenNganhHang NVARCHAR(200)
    
    SET @DsTenNganhHang = ''
    SET @Result = 0
    SET @SoluongHDCT = 1
    SET @v_count_checkthucchay = 0
    SET @DsNganhHangREF = ''
    
	DECLARE Record_Cursor1 CURSOR FOR 
	SELECT DISTINCT tcdt.SoHopDong, tcdt.HopDongID, tcdt.TenNhanVien, tcdt.SysNhanVienREF, tcdt.TenSanPham, tcdt.DmSanPhamREF FROM
	(
		SELECT distinct hd.SoHopDong, hd.HopDongID,hdct.HopDongChiTietID, hd.TenNhanVien, hd.SysNhanVienREF , hdct.TenSanPham, hdct.DmSanPhamREF
		FROM hopdong hd 
		INNER JOIN	HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	)a
	RIGHT JOIN 
	(
		SELECT DISTINCT A.SoHopDong,A.HopDongID, A.HopDongChiTietREF, A.DmSanPhamREF, A.TenSanPham, A.TenNhanVien, A.SysNhanVienREF FROM
		(
			SELECT DISTINCT tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.TenNhanVien, tcdt.SysNhanVienREF
			  FROM ThucChayDaTinh tcdt
			WHERE 1 = 1
			AND (
				tcdt.DmSanPhamREF NOT IN (299,337,299,144,585) AND NOT(tcdt.DmSanPhamREF = 375 AND YEAR(tcdt.NgayThucHien) = 2013)
			)
			AND tcdt.HopDongChiTietREF = 0
			AND tcdt.TrangThaiHopDong <> 3
			--AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF,@NgayThucHien) =0
			AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
			UNION
			SELECT DISTINCT tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.TenNhanVien, tcdt.SysNhanVienREF
			  FROM ThucChayDaTinhAdmarket tcdt
			WHERE 1 = 1
			AND tcdt.DmSanPhamREF IN (299,337,299,144,585,375)
			AND tcdt.HopDongChiTietREF = 0
			AND tcdt.TrangThaiHopDong <> 3
			--AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF,@NgayThucHien) =0
			AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
 
		)A
	) tcdt ON tcdt.HopDongID = a.HopDongID AND a.HopDongChiTietID = tcdt.HopDongChiTietREF

	 
	OPEN Record_Cursor1
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @TenNhanVien, @DmNhanVienREF, @TenSanPham, @DmSanPhamREF 
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
					
					--INSERT DU LIEU CHO TABLE DOANHSOTHUCCHAYNHANHANGCORE
					INSERT INTO RptNhanHangThucChayFull
					SELECT A.DmNhanHangREF,A.TenNhanHang,A.HopDongID,A.SoHopDong
					,A.HopDongChiTietREF,A.DmSanPhamREF,A.TenSanPham
					,0 DmKenhREF
					,'' TenKenh
					,A.NgayThucHien,A.DonViTinh DonViTinh
					,SUM(A.SoLuontThucChay) SoLuongThucChay
				    ,SUM(A.ThucThuPhatSinhTrongKy)ThucThuPhatSinhTrongKy
				    ,'ASD' CreatedBy
				    ,GETDATE() CreatedAt
				    ,0 RecordStatus
					FROM   (
						   SELECT @NgayThucHien NgayThucHien,
								  @DmNhanHangREF DmNhanHangREF,
								  @TenNhanHang TenNhanHang,
								  @DsNganhHangREF DsNganhHangREF,
								  @DsTenNganhHang DsTenNganhHang,
								  tcdt.HopDongID,
								  tcdt.SoHopDong,
								  0 HopDongChiTietREF,
								  tcdt.TenSanPham,
								  tcdt.DmSanPhamREF,
								  tcdt.DonViTinh,
								  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi)/@SoLuongNhan AS SoLuontThucChay,
								  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)/@SoLuongNhan AS 
								  ThucThuPhatSinhTrongKy
								  
							   FROM   ThucChayDaTinh tcdt
							   WHERE tcdt.HopDongID = @HopDongFK
									AND tcdt.DmSanPhamREF = @DmSanPhamREF 
									AND Convert(date,tcdt.NgayThucHien) = @NgayThucHien
							   GROUP BY tcdt.HopDongID,tcdt.SoHopDong, tcdt.HopDongChiTietREF,
									  tcdt.TenSanPham,tcdt.DmSanPhamREF,tcdt.DonViTinh 
							   UNION
							   SELECT @NgayThucHien NgayThucHien,
									  @DmNhanHangREF DmNhanHangREF,
									  @TenNhanHang TenNhanHang,
									  @DsNganhHangREF DsNganhHangREF,
									  @DsTenNganhHang DsTenNganhHang,
									  tcdt.HopDongID,
									  tcdt.SoHopDong,
									  0 HopDongChiTietREF,
									  tcdt.TenSanPham,
									  tcdt.DmSanPhamREF,
									  tcdt.DonViTinh,
									  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi)/@SoLuongNhan AS SoLuontThucChay,
									  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)/@SoLuongNhan AS 
									  ThucThuPhatSinhTrongKy
							   FROM   ThucChayDaTinhAdmarket tcdt
							   WHERE tcdt.HopDongID = @HopDongFK
									AND tcdt.DmSanPhamREF = @DmSanPhamREF 
									AND Convert(date,tcdt.NgayThucHien) = @NgayThucHien
							   GROUP BY tcdt.HopDongID,tcdt.SoHopDong, tcdt.HopDongChiTietREF,
									  tcdt.TenSanPham,tcdt.DmSanPhamREF,tcdt.DonViTinh
						   )A
						WHERE (ROUND(A.ThucThuPhatSinhTrongKy,0) <>0)
					GROUP BY  A.NgayThucHien,A.DmNhanHangREF,A.TenNhanHang,A.HopDongID,A.SoHopDong,
						   A.HopDongChiTietREF,A.TenSanPham,A.DmSanPhamREF, A.DonViTinh
					FETCH NEXT FROM Record_Cursor2 INTO @DmNhanHangREF
				END
				CLOSE Record_Cursor2
				DEALLOCATE Record_Cursor2
			END
			ELSE
				BEGIN
					--INSERT DU LIEU CHO TABLE DOANHSOTHUCCHAYNHANHANGCORE
					INSERT INTO RptNhanHangThucChayFull
					SELECT A.DmNhanHangREF,A.TenNhanHang,A.HopDongID,A.SoHopDong
					,A.HopDongChiTietREF,A.DmSanPhamREF,A.TenSanPham
					,0 DmKenhREF
					,'' TenKenh
					,A.NgayThucHien,A.DonViTinh DonViTinh
					,SUM(A.SoLuontThucChay) SoLuongThucChay
				    ,SUM(A.ThucThuPhatSinhTrongKy)ThucThuPhatSinhTrongKy
				    ,'ASD' CreatedBy
				    ,GETDATE() CreatedAt
				    ,0 RecordStatus
					FROM   (
						   SELECT @NgayThucHien NgayThucHien,
								  @DmNhanHangREF DmNhanHangREF,
								  @TenNhanHang TenNhanHang,
								  @DsNganhHangREF DsNganhHangREF,
								  @DsTenNganhHang DsTenNganhHang,
								  tcdt.HopDongID,
								  tcdt.SoHopDong,
								  0 HopDongChiTietREF,
								  tcdt.TenSanPham,
								  tcdt.DmSanPhamREF,
								  tcdt.DonViTinh,
								  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS SoLuontThucChay,
								  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS 
								  ThucThuPhatSinhTrongKy
								  
							   FROM   ThucChayDaTinh tcdt
							   WHERE tcdt.HopDongID = @HopDongFK
									AND tcdt.DmSanPhamREF = @DmSanPhamREF 
									AND Convert(date,tcdt.NgayThucHien) = @NgayThucHien
							   GROUP BY tcdt.HopDongID,tcdt.SoHopDong, tcdt.HopDongChiTietREF,
									  tcdt.TenSanPham,tcdt.DmSanPhamREF,tcdt.DonViTinh 
							   UNION
							   SELECT @NgayThucHien NgayThucHien,
									  @DmNhanHangREF DmNhanHangREF,
									  @TenNhanHang TenNhanHang,
									  @DsNganhHangREF DsNganhHangREF,
									  @DsTenNganhHang DsTenNganhHang,
									  tcdt.HopDongID,
									  tcdt.SoHopDong,
									  0 HopDongChiTietREF,
									  tcdt.TenSanPham,
									  tcdt.DmSanPhamREF,
									  tcdt.DonViTinh,
									  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS SoLuontThucChay,
									  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS 
									  ThucThuPhatSinhTrongKy
							   FROM   ThucChayDaTinhAdmarket tcdt
							   WHERE tcdt.HopDongID = @HopDongFK
									AND tcdt.DmSanPhamREF = @DmSanPhamREF 
									AND Convert(date,tcdt.NgayThucHien) = @NgayThucHien
							   GROUP BY tcdt.HopDongID,tcdt.SoHopDong, tcdt.HopDongChiTietREF,
									  tcdt.TenSanPham,tcdt.DmSanPhamREF,tcdt.DonViTinh
						   )A
						WHERE (ROUND(A.ThucThuPhatSinhTrongKy,0) <>0)
					GROUP BY  A.NgayThucHien,A.DmNhanHangREF,A.TenNhanHang,A.HopDongID,A.SoHopDong,
						   A.HopDongChiTietREF,A.TenSanPham,A.DmSanPhamREF, A.DonViTinh
					   
				END
		END
		FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @TenNhanVien, @DmNhanVienREF, @TenSanPham, @DmSanPhamREF 
	END
	
	CLOSE Record_Cursor1
	DEALLOCATE Record_Cursor1
	--SELECT '1'
END

--EXEC [Insert_DoanhSoThucChayCoreNhanHang_ThucThu] '2013-12-31'

```
