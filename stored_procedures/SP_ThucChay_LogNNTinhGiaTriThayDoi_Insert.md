# Stored Procedure: `ThucChay_LogNNTinhGiaTriThayDoi_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-10 16:07:02.983000
- **Ngày sửa cuối**: 2015-06-10 16:07:02.983000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@DonGiaCurrent` | `bigint(8)` | No |
| `@SoLuongCurrent` | `int(4)` | No |
| `@DonGiaOld` | `int(4)` | No |
| `@SoLuongOld` | `int(4)` | No |
| `@NoiDungLog` | `nvarchar` | No |
| `@NguonLog` | `nvarchar(1024)` | No |
| `@GhiChu` | `nvarchar` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_LogNNTinhGiaTriThayDoi_Insert] 
	-- Add the parameters for the stored procedure here
	@HopDongREF			INT,
    @SoHopDong			NVARCHAR(50),
    @HopDongChiTietID	INT,
    @DmSanPhamREF		INT,
    @DmWebsiteREF		INT,
    @NgayThucHien		DATETIME,
    @GiaTriThayDoi		FLOAT,
    @DonGiaCurrent		BIGINT,
    @SoLuongCurrent		INT,
    @DonGiaOld			INT,
    @SoLuongOld			INT,
    @NoiDungLog			NVARCHAR(MAX),
    @NguonLog			NVARCHAR(512),
    @GhiChu				NVARCHAR(MAX)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    INSERT INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
      (
        [ThuChay_LogNNTinhGiaTriThayDoiID],
        [HopDongREF],
        [SoHopDong],
        [HopDongChiTietREF],
        [DmSanPhamREF],
        [DmWebsiteREF],
        [NgayThucHien],
        [GiaTriThayDoi],
        [GiaSauCK1],
        [Soluong1],
        [GiaSauCK2],
        [Soluong2],
        [NoiDungLog],
        [NguonLog],
        [GhiChu],
        [CreatedBy],
        [CreatedAt],
        [LastModifiedBy],
        [LastModifiedAt],
        [DeletedStatus],
        [PrintStatus],
        [RecordStatus]
      )
    VALUES
      (
        NEWID(),
        @HopDongREF,
        @SoHopDong,
        @HopDongChiTietID,
        @DmSanPhamREF,
        @DmWebsiteREF,
        @NgayThucHien,
        @GiaTriThayDoi,
        @DonGiaCurrent,
        @SoLuongCurrent,
        @DonGiaOld,
        @SoLuongOld,
        @NoiDungLog,
        @NguonLog,
        @GhiChu,
        'ThucChay',
        GETDATE(),
        'ThucChay',
        GETDATE(),
        0,
        0,
        0
      )
END

```
