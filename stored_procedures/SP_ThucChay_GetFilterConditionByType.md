# Stored Procedure: `ThucChay_GetFilterConditionByType`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-26 10:46:13.520000
- **Ngày sửa cuối**: 2015-08-11 10:04:05.350000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Type` | `nvarchar(100)` | No |
| `@KeyWord` | `nvarchar(510)` | No |
| `@Username` | `nvarchar(100)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql

-- =============================================
-- [ThucChay_GetFilterConditionByType] 'Email', '0984943051', '', '', ''
-- [ThucChay_GetFilterConditionByType] 'PhongBan', N'Tr', '', '', ''
---- =============================================
CREATE PROCEDURE [dbo].[ThucChay_GetFilterConditionByType]
	-- Add the parameters for the stored procedure here
	@Type		NVARCHAR(50),
	@KeyWord	NVARCHAR(255),
	@Username   NVARCHAR(50),
	@StartDate  DATETIME,
	@EndDate    DATETIME
AS
BEGIN
	DECLARE @sql VARCHAR(8000) ='';

	DECLARE @RecordCound INT = '15';    
	
	--IF @Type = 'Email' 
	--	EXEC [ABM_Security].[dbo].[Select_All_User] @KeyWord
	
		--SELECT TOP (@RecordCound) A.HoVaTen, A.Email + ' - ' + A.Mobile AS [text], A.NhanSuSoYeuLyLichID AS [value]
		--FROM NhanSuSoYeuLyLich A
		----WHERE A.Email <> ''  AND (A.Email LIKE N'' + @KeyWord + '%' OR A.Mobile LIKE N'' + @KeyWord + '%' )
		--WHERE (A.Email IS NOT NULL AND A.Email <> '')  AND (A.Mobile IS NOT NULL AND A.Mobile <> '') AND (A.NgayNghiViec IS NULL OR A.NgayNghiViec >= GETDATE()) 
		--	  AND (A.HoVaTen LIKE N'' + @KeyWord + '%' OR A.Email LIKE N'' + @KeyWord + '%' OR A.Mobile LIKE N'' + @KeyWord + '%' )
		--ORDER BY A.HoVaTen 
		
	-- San pham
	IF @Type = 'SanPham' 
		SELECT DISTINCT --TOP (@RecordCound) 
			DmSanPhamREF AS [value], TenSanPham AS [text]
		FROM DmSanPhamThucChay A
		WHERE 1 = 1
			AND A.TenSanPham LIKE N'' + @KeyWord + '%'
			AND A.DeletedStatus = 0		
			AND A.TenSanPham <> '' 
			AND A.TenSanPham IS NOT NULL	
		ORDER BY
			A.TenSanPham;
			
	-- San pham theo Hinh thuc quang cao
	ELSE IF @Type = 'SanPhamHTQC'
		SELECT DISTINCT 
			A.DmSanPhamREF AS [value], A.TenSanPham AS [text]
		FROM DmSanPhamThucChay AS A
		WHERE 
			A.DmHinhThucQuangCao IN (SELECT item FROM dbo.ArrayToTable(dbo.Array(@KeyWord, ',') ) )

			AND A.DeletedStatus = 0
		ORDER BY
			A.TenSanPham;
			
	-- Website
	ELSE IF @Type = 'Website'
		SELECT TOP (@RecordCound)
			A.DmWebsiteReportingdbID AS [value], A.TenWebsite AS [text]
		FROM DmWebsiteReportingdb A 
		WHERE 1 = 1			
			AND A.TenWebsite LIKE N'' + @KeyWord + '%'
			AND A.DeletedStatus = 0
			AND A.TenWebsite <> ''
			AND A.TenWebsite IS NOT NULL
		ORDER BY
			A.TenWebsite;
			
	-- Hop dong
	ELSE IF @Type = 'HopDong'
		SELECT *
		FROM
		(
			SELECT TOP (@RecordCound)
				A.SoHopDong AS [value], A.SoHopDong AS [text]
			FROM HopDong A
			WHERE 1=1
				AND A.SoHopDong LIKE N'' + @KeyWord + '%'
				--AND A.TrangThaiHopDong <> 3
				AND A.DeletedStatus = 0
				AND A.SoHopDong <> ''
			UNION
			SELECT '-' AS [valule], '-' AS [text]
			UNION
			SELECT 'SOHAGAME' AS [valule], 'SOHAGAME' AS [text]
		)T
		ORDER BY
			T.[value];
		
	-- Phong ban
	ELSE IF @Type = 'PhongBan'
		SELECT --TOP (@RecordCound)
			A.DmPhongBanID AS [value], A.TenPhongBan AS [text]
		FROM DmPhongBan A
		WHERE 1 = 1
			AND A.TenPhongBan LIKE N'' + @KeyWord + '%'
			AND A.DeletedStatus = 0
			AND A.TenPhongBan <> ''
			AND A.TenPhongBan IS NOT NULL
		ORDER BY 
			A.TenPhongBan;
			
-- Phong ban
	ELSE IF @Type = 'PhongBan'
		SELECT --TOP (@RecordCound)
			A.DmPhongBanID AS [value], A.TenPhongBan AS [text]
		FROM DmPhongBan A
		WHERE 1 = 1
			AND A.TenPhongBan LIKE N'' + @KeyWord + '%'
			AND A.DeletedStatus = 0
			AND A.TenPhongBan <> ''
			AND A.TenPhongBan IS NOT NULL
		ORDER BY 
			A.TenPhongBan;
			
	-- BoPhan	
	ELSE IF @Type = 'BoPhanNghiepVu'
		SELECT TOP (@RecordCound)
			A.DmBoPhanID AS [value], A.TenBoPhan AS [text]
		FROM dbo.DmBoPhan A
		WHERE 1 = 1
			AND A.TenBoPhan LIKE N'' + @KeyWord + '%'
			AND A.DeletedStatus = 0
			AND A.TenBoPhan <> ''
			AND A.TenBoPhan IS NOT NULL
		ORDER BY 
			A.TenBoPhan;
			
	-- Nhom lam viec
	ELSE IF @Type = 'NhomLamViec'
		SELECT TOP (@RecordCound)
			A.DmNhomLamViecID AS [value], A.TenNhomLamViec AS [text]
		FROM DmNhomLamViec A
		WHERE 1 = 1
			AND A.TenNhomLamViec LIKE N'' + @KeyWord + '%'
			AND A.DeletedStatus = 0
			AND A.TenNhomLamViec <> ''
			AND A.TenNhomLamViec IS NOT NULL
		ORDER BY 
			A.TenNhomLamViec;
			
	-- Phong - Bo phan - Nhom lam viec
	ELSE IF @Type = 'P-B-N'
	BEGIN				
		WITH PBN AS
		(
			SELECT 
				A.DmPhongBanID AS ID, A.TenPhongBan AS NAME,[level] = 1,
				RIGHT('000' + CONVERT(VARCHAR(MAX), DmPhongBanID), 3) AS Lvl
			FROM DmPhongBan A
			WHERE 1 = 1
				AND A.DeletedStatus = 0	
				AND A.TenPhongBan <> ''
				AND A.TenPhongBan IS NOT NULL
			
			UNION ALL
			SELECT 
				B.DmBoPhanID ID, B.TenBoPhan AS NAME, [level] = P.[level] + 1,
				P.lvl + RIGHT('000' + CONVERT(VARCHAR(MAX), P.ID), 3) AS Lvl
			FROM PBN P
				INNER JOIN DmBoPhan B ON B.DmPhongBanFK = P.ID AND P.[level] = 1
			WHERE 1 = 1
				AND B.DeletedStatus = 0
				AND B.TenBoPhan <> ''
				AND B.TenBoPhan IS NOT NULL
				
			UNION ALL
			SELECT 
				N.DmNhomID ID, N.TenNhom NAME, [level] = P1.[level] + 1,
				P1.lvl + RIGHT('000' + CONVERT(VARCHAR(MAX), P1.ID), 3) AS Lvl
			FROM DmNhom N 
				INNER JOIN PBN AS P1 ON N.DmBoPhanREF = P1.ID AND P1.[level] = 2
			WHERE 1 = 1
				AND N.DeletedStatus = 0
				AND N.TenNhom <> ''
				AND N.TenNhom IS NOT NULL
		)
		
		SELECT 
			A.ID AS [value],
			LEFT(REPLICATE('- ', A.[level]) + A.NAME, 512) [text],
			A.[level] AS [typeid] 
		FROM PBN A
		WHERE 1 = 1 
			AND A.NAME LIKE N'%' + @KeyWord + '%'
		ORDER BY
			lvl, A.NAME
		OPTION( MAXRECURSION 0)
	END		
	-- Nhan vien
	ELSE IF @Type = 'NhanVien'
		SELECT TOP (@RecordCound) 
			C.TenDangNhap AS [value], A.HoVaTen AS [text]
		FROM NhanSuSoYeuLyLich A
			INNER JOIN NhanSuQuaTrinhCongTac B ON B.NhanSuSoYeuLyLichREF = A.NhanSuSoYeuLyLichID AND B.[Active] = 1
			INNER JOIN AdminPermisionHDCN C ON C.NhanSuSoYeuLyLichID = A.NhanSuSoYeuLyLichID
		WHERE 1 = 1
			AND A.HoVaTen LIKE N'%' + @KeyWord + '%'
			AND A.DeletedStatus = 0
			AND A.HoVaTen <> ''
			AND A.HoVaTen IS NOT NULL
		ORDER BY 
			A.HoVaTen;
			
	-- Hinh thuc quang cao
	ELSE IF @Type = 'HTQC'
		SELECT TOP (@RecordCound) 
			A.DmHinhThucQuangCaoID AS [value], A.TenHinhThucQuangCao AS [text]
		FROM DmHinhThucQuangCao A
		WHERE 1 = 1
			AND A.TenHinhThucQuangCao LIKE N'' + @KeyWord + '%'
			AND A.DeletedStatus = 0
			AND A.RecordStatus = 1
		ORDER BY 
			A.TenHinhThucQuangCao
			
	-- Hinh thuc quang cao
	ELSE IF @Type = 'HTQC'
		SELECT 
			A.DmHinhThucQuangCaoID AS [value], A.TenHinhThucQuangCao AS [text]
		FROM DmHinhThucQuangCao A
		WHERE 1 = 1
			AND A.TenHinhThucQuangCao LIKE N'' + @KeyWord + '%'
			AND A.DeletedStatus = 0
			AND A.RecordStatus = 1
		ORDER BY 
			A.TenHinhThucQuangCao
				
	-- Banner
	ELSE IF @Type = 'Banner'
		SELECT DISTINCT
			A.DmViTriREF [value], A.TenViTri [text] 
		FROM HopDongChiTiet A
		WHERE 1 = 1
			AND A.TenViTri LIKE N'' + @KeyWord + '%'
			AND DmSanPhamREF IN (306, 423, 535,240) 
			AND DmViTriREF > 0
			AND A.DeletedStatus = 0
			AND ltrim(rtrim(A.TenViTri)) <> ''
		ORDER BY
			A.TenViTri;
			
	-- Don vi tinh
	ELSE IF @Type = 'DonViTinh'
		SELECT -- TOP (@RecordCound)
			A.TenDonViTinh [value], A.TenDonViTinh [text]
		FROM DmDonViTinhThucChay A
		WHERE 1 = 1
			AND A.TenDonViTinh LIKE N'' + @KeyWord + '%'
			AND A.DeletedStatus = 0
			AND A.RecordStatus = 1
		ORDER BY
			A.TenDonViTinh;
			
	-- Khach hang
	ELSE IF @Type = 'KhachHang'
		SELECT TOP (@RecordCound)
			A.KhachHangID [value], A.TenKhachHang [text]
		FROM KhachHangFull A
		WHERE 1 = 1
			AND A.TenKhachHang LIKE N'%' + @KeyWord + '%'
			AND A.DeletedStatus = 0
		ORDER BY
			A.TenKhachHang;	
	
	-- Nhan hang
	ELSE IF @Type = 'NhanHang'
		BEGIN
			DECLARE @IsAdmin  INT,
					@OxUserId INT
					
			SET @OxUserId = (SELECT A.OxUserREF FROM AdminUser A WHERE A.Username =  @Username)
			
			-- Kiểm tra Admin trong bảng AdminGroup
			-- 2, 34			Admin Thực chạy
			-- 106				thunguyenthi
			-- 103 ,151 ,152	Quản lý nhãn
			SET @IsAdmin  = (SELECT COUNT(au.OxUserREF) 
							 FROM AdminGroupUser agu JOIN AdminUser au
							 ON agu.AdminUserId = au.AdminUserId
							 WHERE agu.AdminGroupID IN (2, 34, 103, 106, 151 ,152) AND au.OxUserREF = CONVERT(INT, @OxUserId))
										
			IF(@OxUserId > 0)	
				-- DmNhanHangId							
				IF (@IsAdmin = 0)
					BEGIN
						SELECT TOP (@RecordCound) A.TenNhanHang AS [value], A.TenNhanHang AS [text] FROM DmNhanHang A
						INNER JOIN PhanQuyenNhanHang AS B 
						ON A.DmNhanHangId = B.DmNhanHangREF						
						WHERE A.TenNhanHang LIKE N'%' + @KeyWord + '%' AND B.OxUserREF = @OxUserId AND A.RecordStatus = 1 AND A.DeletedStatus <> 1				
						ORDER BY A.TenNhanHang ASC					
					END		
				ELSE
					BEGIN			
						SELECT TOP (@RecordCound) A.TenNhanHang AS [value], A.TenNhanHang AS [text] FROM DmNhanHang A
						WHERE A.TenNhanHang LIKE N'%' + @KeyWord + '%' AND A.RecordStatus = 1 AND A.DeletedStatus <> 1
						ORDER BY A.TenNhanHang ASC
					END		
		END
		
	-- BookingId
	ELSE IF @Type = 'BookingId'
		BEGIN			
			EXEC dbo.GetDistinctBookingIDFromThucChaySystem @StartDate, @EndDate, '', '', '' -- Chỉ làm ảnh hưởng theo thời gian | @SoHopDongList, @DmBookingREF, @DmBannerREF
		END
		
	-- BannerId
	ELSE IF @Type = 'BannerId'
		BEGIN					
			SELECT DISTINCT DmBannerREF AS [value], DmBannerREF AS [text]
			FROM ThucChay A 
			WHERE CONVERT(DATE,A.NgayThucHien) Between @StartDate AND @EndDate
			GROUP BY DmBannerREF, DmBannerREF
			ORDER BY DmBannerREF ASC	
		END
END

```
