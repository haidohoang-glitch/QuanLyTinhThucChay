# Stored Procedure: `ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-08 11:29:22.853000
- **Ngày sửa cuối**: 2015-07-10 14:01:29.917000

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
	EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarket '2015-01-06'
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarket]
	-- Add the parameters for the stored procedure here
	@ngayThucHien	DateTime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	DECLARE @ngayGioiHanTinh DATETIME = '2014-09-30',
			@startDate			DATETIME,
			@endDate			DATETIME,
			@ghiChu				NVARCHAR(255) = N'Admarket_Chay_Lai_Du_Lieu',
			@dmViTriREF			INT,
			@tenViTri			NVARCHAR(50)	

	DECLARE @account	NVARCHAR(50),
			@sanPhamId	INT,
			@donViTinh	NVARCHAR(50) = 'CLICK'

	DECLARE @money		FLOAT,
			@promotion	FLOAT

	DECLARE @tienThucChayDaTinh	FLOAT,
			@tienKMDaTinh		FLOAT,
			@soLuongThucChayDaTinh		INT
			
	SET @ngayThucHien = CONVERT(date,@NgayThucHien);

	DECLARE acc_cursor CURSOR FOR
	SELECT DISTINCT TK_AdMarket, DmSanPhamREF 
	FROM HopDongChiTiet A
	WHERE 1=1
		AND A.DmSanPhamREF IN (144, 299, 337, 585)
		AND CONVERT(DATE,A.CreatedAt) = @ngayThucHien
		--AND A.TK_AdMarket = 'djbuonvn'
		--AND (CASE WHEN A.LastModifiedBy <> '' and A.LastModifiedBy <> 'ABM_SERVICE' THEN CONVERT(DATE, A.LastModifiedAt)
		--		ELSE CONVERT(DATE, A.CreatedAt)
		--	END) = @ngayThucHien

	OPEN acc_cursor;

	FETCH NEXT FROM acc_cursor INTO @account, @sanPhamId

	WHILE @@FETCH_STATUS = 0
	BEGIN
		SELECT @account, @sanPhamId
		--IF @sanPhamId = 585
		--BEGIN
		--	PRINT 'sanPhamID: ' + CONVERT(NVARCHAR(50), @sanPhamId) 
		--	SELECT @money = ISNULL(SUM([money]/1.1),0),
		--			@promotion = ISNULL(SUM(A.pro/1.1),0)
		--	FROM ThucChayAdXForUsers A
		--	WHERE 1=1
		--		AND A.username = @account
		--		AND A.DmSanPhamREF = @sanPhamId
		--END
		--ELSE
		--BEGIN
		--	PRINT 'sanPhamID: ' + CONVERT(NVARCHAR(50), @sanPhamId) 
		--	SELECT @money = ISNULL(SUM([money]/1.1),0),
		--			@promotion = ISNULL(SUM(A.pro/1.1),0)
		--	FROM ThucChayAdmarketUsers A
		--	WHERE 1=1
		--		AND A.username = @account
		--		AND A.DmSanPhamREF = @sanPhamId
		--END
		
		PRINT '@money: ' + CONVERT(NVARCHAR(50), @money) 
		PRINT '@promotion: ' + CONVERT(NVARCHAR(50), @promotion)
		
		IF @sanPhamId = 585
		BEGIN		
			DECLARE vitri_cursor CURSOR FOR
			SELECT DISTINCT DmViTriREF, TenViTri
			FROM ThucChayAdXForUsers A
			WHERE 1=1
				AND A.username = @account
				AND A.NgayThucHien <= @ngayThucHien
		END
		ELSE
		BEGIN
			PRINT 'CPC Admarket'
			DECLARE vitri_cursor CURSOR FOR
			SELECT TOP 1 1 as DmViTriREF, '' as TenViTri
			FROM ThucChayAdmarketUsers A
			WHERE 1=1
				AND A.username = @account
				AND A.NgayThucHien <= @ngayThucHien
		END
		OPEN vitri_cursor
		
		FETCH NEXT FROM vitri_cursor INTO @dmViTriREF, @tenViTri
		
		WHILE @@FETCH_STATUS = 0
		BEGIN 
			PRINT 'DmViTriREF: ' + CONVERT(NVARCHAR(50), @dmViTriREF)
		
			/*
				Check xem tai khoan da duoc tinh thuc chay ngay nao chua
				Day la truong hop tai khoan chua duoc tinh thuc chay
			*/
			IF NOT EXISTS(
							SELECT HopDongID, A.HopDongChiTietREF
							FROM ThucChayDaTinhAdmarket A
							WHERE 1=1
								AND A.DmSanPhamREF = @sanPhamID
								AND A.HopDongChiTietREF IN (SELECT HopDongChiTietID 
																FROM HopDongChiTiet 
																WHERE TK_Admarket = @account)
								AND A.NgayThucHien < @ngayThucHien
								AND A.DmViTriREF = @dmViTriREF
							)
			BEGIN
				PRINT 'Chua ton tai';
				IF (@sanPhamID = 585)
				BEGIN
					SELECT 
						@startDate  = MIN(A.NgayThucHien),
						@endDate	= DATEADD(d,-1, @ngayThucHien)
					FROM ThucChayAdXForUsers A
					WHERE 1=1
						AND A.username = @account
						AND A.DmSanPhamREF = @sanPhamId
						AND A.DmViTriREF = @dmViTriREF
				END
				ELSE
				BEGIN
					PRINT 'CPC Admarket 111'
					SELECT 
						@startDate  = MIN(A.NgayThucHien),
						@endDate	= DATEADD(d,-1, @ngayThucHien)
					FROM ThucChayAdmarketUsers A
					WHERE 1=1
						AND A.username = @account
						AND A.DmSanPhamREF = @sanPhamId
						--AND A.DmViTriREF = @dmViTriREF
				END

				PRINT '@startDate: ' + CONVERT(NVARCHAR(50), @startDate);
				PRINT '@endDate: ' + CONVERT(NVARCHAR(50), @endDate);
				-- Insert data nguon de tinh thuc chay
				EXEC [dbo].[ThucChaySelfServingUsers_InsertByAccountAndProduct]
					@startDate, @endDate, @ngayThucHien, @account, @sanPhamId, @dmViTriREF, @tenViTri

				select * from ThucChaySelfServingUsers
			END
			/*		
				Nguoc lai thuc chay da duoc tinh mot phan
			*/
			ELSE
			BEGIN
				PRINT 'Da ton tai';
			
				SELECT @startDate = MIN(NgayThucHien),
					@endDate = MAX(NgayThucHien)
				FROM ThucChayAdmarketOnline A
				WHERE 1=1
					AND A.RecordStatus = 0
					AND A.DmSanPhamREF = @sanPhamID
					AND A.TaiKhoan = @account
					AND A.NgayThucHien <= @ngayThucHien
					AND A.DmViTriREF = @dmViTriREF

				PRINT '@startDate: ' + CONVERT(NVARCHAR(50), @startDate);
				PRINT '@endDate: ' + CONVERT(NVARCHAR(50), @endDate);

				TRUNCATE TABLE ThucChaySelfServingUsers;

				INSERT INTO ThucChaySelfServingUsers
				SELECT 
					NEWID() ThucChaySelfServingUsersID
					,A.TaiKhoan
					,A.DmSanPhamREF
					,A.TenSanPham
					,'' Domain
					,SUM(SoLuong) [ttc]
					--,SUM(SoLuong) [ttv]
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
					,DmViTriREF
					,TenViTri
				FROM ThucChayAdmarketOnline A
				WHERE 1=1
					AND A.RecordStatus = 0
					AND A.DmSanPhamREF = @sanPhamID
					AND A.TaiKhoan = @account
					AND A.NgayThucHien <= @ngayThucHien
					AND A.DmViTriREF = @dmViTriREF
					AND (SELECT COUNT(tcdta.HopDongChiTietREF)
		               FROM ThucChayDaTinhAdmarket tcdta WHERE tcdta.NgayThucHien = @NgayThucHien
					AND tcdta.DmSanPhamREF = A.DmSanPhamREF 
					AND tcdta.HopDongChiTietREF IN (SELECT HopDongChiTietID FROM HopDongChiTiet WHERE HopDongChiTiet.TK_AdMarket =@account)
					AND tcdta.GhiChu = N'Update thấu chi') <=0
				GROUP BY
					A.TaiKhoan
					,A.DmSanPhamREF
					,A.TenSanPham
					,IsNoiBo
					,DonViTinh
					,DmViTriREF
					,TenViTri
				-- Insert data nguon de tinh thuc chay
				--EXEC [dbo].[ThucChaySelfServingUsers_InsertByAccountAndProduct]
				--	@startDate, @endDate, @ngayThucHien, @account, @sanPhamId
				
				--select * from ThucChaySelfServingUsers

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
			END

			IF (@sanPhamId = 585 OR @sanPhamId = 144)
				SET @donViTinh = 'CLICK'

			/*
				Insert Thuc chay Admarket
			*/
			
			EXEC dbo.ThucChayDaTinh_InsertThucChayDaTinhAdmarket
				@ngayThucHien,
				@sanPhamId,
				@account,
				@donViTinh,
				@ghiChu,
				@dmViTriREF,
				@tenViTri
		
			FETCH NEXT FROM vitri_cursor INTO @dmViTriREF, @tenViTri
		END
		
		CLOSE vitri_cursor
		DEALLOCATE vitri_cursor

		FETCH NEXT FROM acc_cursor INTO @account, @sanPhamId
	END

	CLOSE acc_cursor;
	DEALLOCATE acc_cursor;
END

```
