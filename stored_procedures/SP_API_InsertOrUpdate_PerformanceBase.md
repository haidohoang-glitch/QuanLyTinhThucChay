# Stored Procedure: `API_InsertOrUpdate_PerformanceBase`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-02-24 16:04:32.037000
- **Ngày sửa cuối**: 2024-07-01 16:04:56.647000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PhanBoId` | `int(4)` | No |
| `@SanPhamId` | `int(4)` | No |
| `@ViTriId` | `int(4)` | No |
| `@TaiKhoan` | `nvarchar(1000)` | No |
| `@RequestKey` | `nvarchar(1000)` | No |
| `@TienThayDoi` | `float(8)` | No |
| `@NgayThayDoi` | `datetime(8)` | No |
| `@TienThucChayKPI` | `float(8)` | No |
| `@LoaiGhiNhan` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[API_InsertOrUpdate_PerformanceBase]
    -- Add the parameters for the stored procedure here
    @PhanBoId INT = NULL,
    @SanPhamId INT = NULL,
    @ViTriId INT = NULL,
    @TaiKhoan NVARCHAR(500),
    @RequestKey NVARCHAR(500),
    @TienThayDoi FLOAT,
    @NgayThayDoi DATETIME,
	@TienThucChayKPI FLOAT = 0,
	@LoaiGhiNhan INT = 0
AS
BEGIN
    IF EXISTS (SELECT 1 FROM dbo.ThucChay_PerformanceBase_ThayDoi WHERE UPPER(Request_key) = UPPER(@RequestKey)
              AND ISNULL(DeletedStatus, 0) = 0 )
		BEGIN
			DECLARE @status INT;
			DECLARE @id BIGINT;

			SELECT @status = RecordStatus, @id = Id
			FROM dbo.ThucChay_PerformanceBase_ThayDoi
			WHERE UPPER(Request_key) = UPPER(@RequestKey) AND ISNULL(DeletedStatus, 0) = 0

			IF(ISNULL(@status, 0) = 0)
			BEGIN
				 UPDATE dbo.ThucChay_PerformanceBase_ThayDoi
				SET TK_Admarket = @TaiKhoan,
					SoTienThayDoi = @TienThayDoi,
					NgayGhiNhanThayDoi = @NgayThayDoi,
					LastModifiedAt = GETDATE(),
					LastModifiedBy = 'API_SanPham',
					HopDongChiTietREF = @PhanBoId,
					DmSanPhamREF = @SanPhamId,
					DmViTriREF = @ViTriId,
					TienThucChayKPI = @TienThucChayKPI,
					LoaiGhiNhan = @LoaiGhiNhan
				WHERE Id = @id;

				SELECT 1 AS Id;
			END ELSE 
			BEGIN
				/** da ghi nhan roi thi khong cho update */
				SELECT -1 AS Id;
			END
		END;
    ELSE
		BEGIN
			DECLARE @hopDongId INT;
			DECLARE @soHopDong NVARCHAR(100);

			SELECT @hopDongId = HopDongFK
			FROM dbo.HopDongChiTiet
			WHERE HopDongChiTietID = @PhanBoId

			SELECT @soHopDong = SoHopDong
			FROM dbo.HopDong
			WHERE HopDongID = @hopDongId


			INSERT INTO dbo.ThucChay_PerformanceBase_ThayDoi
			(
				Request_key,
				SoHopDong,
				HopDongID,
				HopDongChiTietREF,
				DmSanPhamREF,
				TenSanPham,
				TK_Admarket,
				ThanhTien,
				DmViTriREF,
				TenViTri,
				TienThucChayTong,
				TienThucChay,
				ThucChayDenNgay,
				SoTienThayDoi,
				NgayGhiNhanThayDoi,
				CreatedAt,
				CreatedBy,
				LastModifiedAt,
				LastModifiedBy,
				RecordStatus,
				LyDoTuChoi,
				DeletedStatus,
				TienThucChayKPI,
				LoaiGhiNhan
			)
			VALUES
			(   @RequestKey,    -- Request_key - nvarchar(50)
				@soHopDong,     -- SoHopDong - nvarchar(50)
				@hopDongId,     -- HopDongID - int
				@PhanBoId,      -- HopDongChiTietREF - int
				@SanPhamId,     -- DmSanPhamREF - int
				N'',            -- TenSanPham - nvarchar(50)
				@TaiKhoan,      -- TK_Admarket - nvarchar(50)
				0.0,            -- ThanhTien - float
				@ViTriId,       -- DmViTriREF - int
				CASE
					WHEN @ViTriId = 1 THEN
						'AdX'
					WHEN @ViTriId = 2 THEN
						'AdX Mobile'
					WHEN @ViTriId = 3 THEN
						'AdX Ecommerce'
				    WHEN @ViTriId = 4 THEN
						'AdX Leadform'
					WHEN @ViTriId = 0 THEN
						''
					ELSE
						''
				END,            -- TenViTri - nvarchar(50)
				NULL,            -- TienThucChayTong - float
				NULL,            -- TienThucChay - float
				NULL,           -- ThucChayDenNgay - datetime
				@TienThayDoi,   -- SoTienThayDoi - float
				@NgayThayDoi,   -- NgayGhiNhanThayDoi - datetime
				GETDATE(),      -- CreatedAt - datetime
				N'API_SanPham', -- CreatedBy - nvarchar(50)
				GETDATE(),      -- LastModifiedAt - datetime
				N'API_SanPham', -- LastModifiedBy - nvarchar(50)
				0,              -- RecordStatus - int
				N'',            -- LyDoTuChoi - nvarchar(200)
				0,               -- DeletedStatus - bit
				@TienThucChayKPI,
				@LoaiGhiNhan
				);

				SELECT 1 AS Id;
		END;

END;

```
