# Stored Procedure: `ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarketFromOnlineData`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-10 16:07:03.930000
- **Ngày sửa cuối**: 2015-07-09 14:31:28.503000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-11-08
-- Description:	<Description,,>
-- =============================================

/*
	EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarketFromOnlineData '2015-01-18'
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarketFromOnlineData]
	-- Add the parameters for the stored procedure here
	@ngayThucHien	DateTime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	DECLARE @ngayGioiHanTinh DATETIME = '2013-01-01'
	
	DECLARE @account	NVARCHAR(50),
		@sanPhamId	INT,
		@tenSanPham	NVARCHAR(50),
		@soLuongOnline	BIGINT,
		@tienThucChayOnline	FLOAT,
		@tienKhuyenMaiOnline	FLOAT,
		@contentLog	NVARCHAR(512) = 'ThucChay_Admarket_Chay_Lai_Du_Lieu_Online',
		@ghiChu		NVARCHAR(512) = 'ThucChay_Admarket_Chay_Lai_Du_Lieu_Online',
		@donViTinh	NVARCHAR(512) = 'CLICK',
		@dmViTriREF	INT,
		@tenViTri	NVARCHAR(512)
		
	DECLARE acc_cursor CURSOR FOR
	SELECT 
		A.TaiKhoan, A.DmSanPhamREF, A.TenSanPham,
		SUM(CAST(A.SoLuong AS BIGINT)) SoLuongOnline,
		SUM(A.TienThucChay) TienThucChayOnline,
		SUM(A.TienKhuyenMai) TienKhuyenMaiOnline,
		A.DmViTriREF,
		A.TenViTri
	FROM ThucChayAdmarketOnline A
	WHERE 1=1
		AND A.RecordStatus = 0
		AND A.TienThucChay > 0
		AND A.NgayThucHien <= @ngayThucHien
		AND (SELECT COUNT(tcdta.HopDongChiTietREF)
		       FROM ThucChayDaTinhAdmarket tcdta WHERE tcdta.NgayThucHien = @NgayThucHien
					AND tcdta.DmSanPhamREF = A.DmSanPhamREF 
					AND tcdta.HopDongChiTietREF IN (SELECT HopDongChiTietID FROM HopDongChiTiet WHERE HopDongChiTiet.TK_AdMarket =A.TaiKhoan)
					AND tcdta.GhiChu = N'Update thấu chi') <=0
		--AND A.TaiKhoan = 'tienganh123'
	GROUP BY
		A.TaiKhoan, A.DmSanPhamREF, A.TenSanPham, A.DmViTriREF, A.TenViTri
		
	OPEN acc_cursor

	FETCH NEXT FROM acc_cursor INTO @account, @sanPhamId, @tenSanPham, @soLuongOnline, @tienThucChayOnline, @tienKhuyenMaiOnline, @dmViTriREF, @TenViTri
	WHILE @@FETCH_STATUS = 0
	BEGIN
		--SELECT @account, @sanPhamId, @tenSanPham, @soLuongOnline, @tienThucChayOnline, @tienKhuyenMaiOnline
		--IF EXISTS(
		--	SELECT 
		--		T.*
		--	FROM
		--	(
		--		SELECT A.HopDongChiTietID, 
		--			--A.ThanhTien, 
		--			dbo.ThucChay_GetTienVeByPhanBoID(A.HopDongFK, A.HopDongChiTietID, @ngayThucHien) ThanhTien,
		--			ISNULL(B.ThanhTienThucChay,0) ThanhTienThucChay
		--		FROM HopDongChiTiet A
		--			LEFT JOIN
		--			(
		--				SELECT HopDongChiTietREF,
		--					ROUND(SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)),0) ThanhTienThucChay
		--				FROM ThucChayDaTinhAdmarket tcdt
		--				WHERE 1=1
		--					AND tcdt.DmSanPhamREF = @sanPhamId
		--				GROUP BY HopDongChiTietREF
		--			) B ON B.HopDongChiTietREF = A.HopDongChiTietID
		--		WHERE 1=1	
		--			AND A.TK_AdMarket = @account
		--			AND A.DmSanPhamREF = @sanPhamId
		--	)T
		--	WHERE 1=1
		--		AND T.ThanhTien > T.ThanhTienThucChay
		--)
		--BEGIN			
			-- Insert Du lieu nguon de tinh thuc chay	
			TRUNCATE TABLE ThucChaySelfServingUsers;
			INSERT INTO ThucChaySelfServingUsers
			SELECT 
				NEWID() ThucChaySelfServingUsersID
				,A.TaiKhoan
				,A.DmSanPhamREF
				,A.TenSanPham
				,'' Domain
				,SUM(SoLuong) [ttc]
				--,SUM(TotalView) [ttv]
				,0 [ttv]
				,SUM(TienThucChay*1.1) TienThucChay
				,SUM(TienKhuyenMai*1.1) TienKhuyenMai
				,ISNULL(IsNoiBo,0) IsNoiBo
				,@ngayThucHien
				,GETDATE() CreatedAt
				,'asd' CreatedBy
				,GETDATE() LastModifiedAt
				,'asd' LastModifiedBy
				,0 UserId
				,DonViTinh
				,A.DmViTriREF
				,A.TenViTri
			FROM ThucChayAdmarketOnline A
			WHERE 1=1
				AND A.RecordStatus = 0
				AND A.DmSanPhamREF = @sanPhamID
				AND A.TaiKhoan = @account
				AND A.NgayThucHien <= @ngayThucHien
				AND A.DmViTriREF = @dmViTriREF
			GROUP BY
				A.TaiKhoan
				,A.DmSanPhamREF
				,A.TenSanPham
				,IsNoiBo
				,DonViTinh
				,A.DmViTriREF
				,A.TenViTri
				
			-- Update status du lieu online
			UPDATE ThucChayAdmarketOnline
			SET RecordStatus = 1,
				LastModifiedAt = GETDATE()
			WHERE 1=1
				AND RecordStatus = 0
				AND DmSanPhamREF = @sanPhamID
				AND TaiKhoan = @account
				AND NgayThucHien <= @ngayThucHien
				AND DmViTriREF = @dmViTriREF
				
			/*
				Insert Thuc chay Admarket
			*/
			EXEC dbo.ThucChayDaTinh_ReInsertThucChayDaTinhAdmarket
				@ngayThucHien,
				@sanPhamId,
				@account,
				@donViTinh,
				@ghiChu,
				@dmViTriREF,
				@tenViTri
				
		--END
		
		FETCH NEXT FROM acc_cursor INTO @account, @sanPhamId, @tenSanPham, @soLuongOnline, @tienThucChayOnline, @tienKhuyenMaiOnline, @dmViTriREF, @TenViTri
	END

	CLOSE acc_cursor
	DEALLOCATE acc_cursor

END

```
