# Stored Procedure: `ThucChay_UpdateGiaTriThayDoi_HDDaChayDuSoLuong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-11 09:53:31.217000
- **Ngày sửa cuối**: 2015-03-11 09:53:31.217000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[ThucChay_UpdateGiaTriThayDoi_HDDaChayDuSoLuong] 

CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoi_HDDaChayDuSoLuong] 
AS
BEGIN
	DECLARE @SoHopDong NVARCHAR(50), @NgayThucHienMin DATETIME, @NgayThucHienMax DATETIME
	DECLARE @DmSanPhamREF INT
	
	SET @SoHopDong = ''
	SET @NgayThucHienMin = GETDATE()
	SET @NgayThucHienMax = GETDATE()
	SET @DmSanPhamREF = 0
	
	DECLARE Record_Cursor_TCDT1 CURSOR  FOR
		-- -- Danh sach 1 
		--SELECT A.*
		--	--, B.F4 TenSanpham
		--FROM   (
		--		   SELECT tc.sohopdong sohopdong,
		--				  convert(date,MIN(tc.ngaythuchien))ngaythuchienMin,
		--				  convert(date,MAX(tc.ngaythuchien)) ngaythuchienMax,
		--				  (
		--					  CASE 
		--						   WHEN tc.TypeProduct = 3 THEN 231
		--						   WHEN tc.TypeProduct = 4 THEN 238
		--						   WHEN tc.TypeProduct = 5 THEN 339
		--						   WHEN tc.TypeProduct = 8 THEN 240
		--						   WHEN tc.TypeProduct = 9 THEN 370
		--						   WHEN tc.TypeProduct = 14 THEN 598
		--						   WHEN tc.TypeProduct = 15 THEN 613
		--					  END
		--				  ) DmSanphamREF
		--		   FROM   ABM_Phuongtt.dbo.ThucChayThem1 tc
		--		   WHERE  TypeProduct IN (3, 4, 5, 8, 9, 14, 15)
		--		   GROUP BY
		--				  tc.SoHopDong,
		--				  tc.TypeProduct
		--	   ) A
		--	  -- INNER JOIN ThucChayCPM.dbo.[CPMTinhLai$] B
		--			--ON  A.Sohopdong = B.F1
		--			--AND A.DmSanPhamREF = B.F3
		--WHERE 1=1
		 
		-- -- Danh sach 2
		--SELECT A.*
		--	--, B.F4 TenSanpham
		--FROM   (
		--		   SELECT tc.sohopdong sohopdong,
		--				  convert(date,MIN(tc.ngaythuchien))ngaythuchienMin,
		--				  convert(date,MAX(tc.ngaythuchien)) ngaythuchienMax,
		--				  (
		--					  CASE 
		--						   WHEN tc.TypeProduct = 3 THEN 231
		--						   WHEN tc.TypeProduct = 4 THEN 238
		--						   WHEN tc.TypeProduct = 5 THEN 339
		--						   WHEN tc.TypeProduct = 8 THEN 240
		--						   WHEN tc.TypeProduct = 9 THEN 370
		--						   WHEN tc.TypeProduct = 14 THEN 598
		--						   WHEN tc.TypeProduct = 15 THEN 613
		--					  END
		--				  ) DmSanphamREF
		--		   FROM   ABM_Phuongtt.dbo.ThucChayThem1 tc
		--		   WHERE  TypeProduct IN (3, 4, 5, 8, 9, 14, 15)
		--		   GROUP BY
		--				  tc.SoHopDong,
		--				  tc.TypeProduct
		--	   ) A
		--	   INNER JOIN 
		--	    ( SELECT tc.sohopdong sohopdong,
		--				  (
		--					  CASE 
		--						   WHEN tc.TypeProduct = 3 THEN 231
		--						   WHEN tc.TypeProduct = 4 THEN 238
		--						   WHEN tc.TypeProduct = 5 THEN 339
		--						   WHEN tc.TypeProduct = 8 THEN 240
		--						   WHEN tc.TypeProduct = 9 THEN 370
		--						   WHEN tc.TypeProduct = 14 THEN 598
		--						   WHEN tc.TypeProduct = 15 THEN 613
		--					  END
		--				  ) DmSanphamREF
		--		   FROM   ThucChayCPM.dbo.[CPMTinhLai3$] tc
		--		   WHERE  TypeProduct IN (3, 4, 5, 8, 9, 14, 15)
		--		   GROUP BY
		--				  tc.SoHopDong,
		--				  tc.TypeProduct
		--		)B
		--			ON  A.Sohopdong = B.Sohopdong
		--			AND A.DmSanPhamREF = B.DmSanphamREF
		--WHERE 1=1 

		--3 Chay danh sach thay doi thuc treo Banner
		
		--SELECT DISTINCT A.* 
		--FROM 
		--(
		--SELECT d.SoHopDong, '2014-12-31' NgayThucHienMin , '2014-12-31' NgayThucHienMax, d.DmSanPhamREF  
		--FROM dbo.DSXoaDLThucChayHopDongChiTiet d
		--UNION ALL
		--SELECT hd.SoHopDong,'2014-12-31' NgayThucHienMin , '2014-12-31' NgayThucHienMax,dtt.DmSanPhamREF
		--FROM [DSInsertThucTreo] dtt
		--INNER JOIN HopDong hd ON dtt.HopDongREF = hd.HopDongID
		--)A
		--ORDER BY A.SoHopDong,a.DmSanPhamREF
		
		--4 CHAY HAM CHO VIEC THAY DOI SO LUONG HD
		
		SELECT distinct tcdt.SoHopDong, '2014-12-31' NgayThucHienMin,'2014-12-31' NgayThucHienMax, tcdt.DmSanPhamREF  
		  FROM ThucChayDaTinh tcdt
		WHERE tcdt.SoHopDong = 'QC1310714'
		AND tcdt.DmSanPhamREF =240
		AND tcdt.TrangThaiHopDong <> 3
		AND tcdt.HopDongChiTietREF = 61380




	OPEN Record_Cursor_TCDT1
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_TCDT1 INTO @SoHopDong, @NgayThucHienMin, @NgayThucHienMax, @DmSanPhamREF
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT @SoHopDong
		EXEC dbo.[ThucChay_ExcInsertThucChayDaTinhBySoHopDong] @NgayThucHienMin, @NgayThucHienMax, @SoHopDong, @DmSanPhamREF
	    FETCH NEXT FROM Record_Cursor_TCDT1 INTO @SoHopDong, @NgayThucHienMin, @NgayThucHienMax, @DmSanPhamREF
	END
	CLOSE Record_Cursor_TCDT1
	DEALLOCATE Record_Cursor_TCDT1
	SELECT 1
END

```
