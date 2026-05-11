# Stored Procedure: `Insert_RptNhanHangThucChayFull_ThucThuKhuyenMai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-02-10 10:42:12.223000
- **Ngày sửa cuối**: 2015-02-12 10:43:35.667000

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

--EXEC [Insert_DoanhSoThucChayNhanHangCore_ThucThu] '2013-12-31'

CREATE  PROCEDURE [dbo].[Insert_RptNhanHangThucChayFull_ThucThuKhuyenMai] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @Result BIGINT, @SoHopDong NVARCHAR(50),@HopDongFK INT,@HopDongChiTietID INT
	DECLARE @TenSanPham NVARCHAR(100), @DmSanPhamREF INT, @LstDmNhanHangREF NVARCHAR(200) 
    DECLARE @DoanhSoThucChay BIGINT, @CheckHopDongChiTietTcID INT 
    DECLARE @DmNhanHangREF INT, @TenNhanHang NVARCHAR(200), @SoluongHDCT INT, @SoLuongNhan INT
    DECLARE @v_count_checkthucchay INT
    DECLARE @DsNganhHangREF NVARCHAR(50), @TenNhanVien NVARCHAR(300), @DmNhanVienREF INT
    DECLARE @DsTenNganhHang NVARCHAR(200)
    
    SET @DsTenNganhHang = ''
    SET @Result = 0
    SET @SoluongHDCT = 1
    SET @v_count_checkthucchay = 0
    SET @DsNganhHangREF = ''
    
	DECLARE Record_Cursor1 CURSOR FOR 
	SELECT DISTINCT tcdt.SoHopDong, tcdt.HopDongID, tcdt.TenNhanVien, tcdt.SysNhanVienREF, tcdt.HopDongChiTietREF, tcdt.TenSanPham, tcdt.DmSanPhamREF, isnull(a.DanhSachNhanHangREF,'')DanhSachNhanHangREF
	  FROM
	(
		SELECT distinct hd.SoHopDong, hd.HopDongID,hdct.HopDongChiTietID, hdct.DanhSachNhanHangREF
		FROM hopdong hd 
		INNER JOIN	HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		--WHERE hd.TrangThaiHopDong <> 3
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
			AND tcdt.HopDongID <> 0
			AND tcdt.HopDongChiTietREF <> 0
			AND tcdt.TrangThaiHopDong <> 3
			--AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF,@NgayThucHien) =0
			AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
			UNION
			SELECT DISTINCT tcdt.SoHopDong,tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.TenNhanVien, tcdt.SysNhanVienREF
			  FROM ThucChayDaTinhAdmarket tcdt
			WHERE 1 = 1
			AND tcdt.DmSanPhamREF IN (299,337,299,144,585,375)
			AND tcdt.HopDongID <>0
			AND tcdt.HopDongChiTietREF <> 0
			AND tcdt.TrangThaiHopDong <> 3
			--AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF,@NgayThucHien) =0
			AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
 
		)A
	) tcdt ON tcdt.HopDongID = a.HopDongID AND a.HopDongChiTietID = tcdt.HopDongChiTietREF

	OPEN Record_Cursor1
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @TenNhanVien, @DmNhanVienREF, @HopDongChiTietID, @TenSanPham, @DmSanPhamREF, @LstDmNhanHangREF
	WHILE @@FETCH_STATUS = 0
	BEGIN
		--Check hop dong, san pham co thuc chay ngay
		BEGIN
			--PRINT @LstDmNhanHangREF
			SET @DmNhanHangREF = 0
			SET @TenNhanHang = ''
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
					
					SELECT @CheckHopDongChiTietTcID = COUNT(A.HopDongChiTietREF) FROM 
					(
					SELECT DISTINCT tcdt.HopDongChiTietREF
						  FROM ThucChayDaTinh tcdt
						WHERE tcdt.HopDongID = @HopDongFK
						AND tcdt.HopDongChiTietREF = 0
						AND tcdt.DmSanPhamREF = @DmSanPhamREF 
						AND Convert(date,tcdt.NgayThucHien) = @NgayThucHien
					)A

					IF(@CheckHopDongChiTietTcID = 0)--Neu HopDongChiTietID <> 0
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
										  tcdt.HopDongChiTietREF HopDongChiTietREF,
										  tcdt.TenSanPham,
										  tcdt.DmSanPhamREF,
										  tcdt.DonViTinh,
										  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi)/@SoLuongNhan AS SoLuontThucChay,
										  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)/@SoLuongNhan AS 
										  ThucThuPhatSinhTrongKy
										  
								   FROM   ThucChayDaTinh tcdt
								   WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
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
										  tcdt.HopDongChiTietREF HopDongChiTietREF,
										  tcdt.TenSanPham,
										  tcdt.DmSanPhamREF,
										  tcdt.DonViTinh,
										  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi)/@SoLuongNhan AS SoLuontThucChay,
										  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)/@SoLuongNhan AS 
										  ThucThuPhatSinhTrongKy
								   FROM   ThucChayDaTinhAdmarket tcdt
								   WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
										AND tcdt.DmSanPhamREF = @DmSanPhamREF 
										AND Convert(date,tcdt.NgayThucHien) = @NgayThucHien
								   GROUP BY tcdt.HopDongID,tcdt.SoHopDong, tcdt.HopDongChiTietREF,
										  tcdt.TenSanPham,tcdt.DmSanPhamREF,tcdt.DonViTinh
							   )A
							WHERE (ROUND(A.ThucThuPhatSinhTrongKy,0) <>0)
						GROUP BY  A.NgayThucHien,A.DmNhanHangREF,A.TenNhanHang,A.HopDongID,A.SoHopDong,
							   A.HopDongChiTietREF,A.TenSanPham,A.DmSanPhamREF, A.DonViTinh
						END
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
									  tcdt.HopDongChiTietREF HopDongChiTietREF,
									  tcdt.TenSanPham,
									  tcdt.DmSanPhamREF,
									  tcdt.DonViTinh,
									  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi)/@SoLuongNhan AS SoLuontThucChay,
									  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)/@SoLuongNhan AS 
									  ThucThuPhatSinhTrongKy
									  
							   FROM   ThucChayDaTinh tcdt
							   WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
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
									  tcdt.HopDongChiTietREF HopDongChiTietREF,
									  tcdt.TenSanPham,
									  tcdt.DmSanPhamREF,
									  tcdt.DonViTinh,
									  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS SoLuontThucChay,
									  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS 
									  ThucThuPhatSinhTrongKy
							   FROM   ThucChayDaTinhAdmarket tcdt
							   WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
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
		FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @TenNhanVien, @DmNhanVienREF, @HopDongChiTietID, @TenSanPham, @DmSanPhamREF, @LstDmNhanHangREF
	END
	
	CLOSE Record_Cursor1
	DEALLOCATE Record_Cursor1
	--SELECT '1'
END

--EXEC [Insert_DoanhSoThucChayCoreNhanHang_ThucThu] '2013-12-31'

```
