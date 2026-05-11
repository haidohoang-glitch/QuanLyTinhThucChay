# Stored Procedure: `usp_InsertNhanSuSoYeuLyLich`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.660000
- **Ngày sửa cuối**: 2014-10-14 10:39:45.907000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuSoYeuLyLichID` | `int(4)` | No |
| `@MaNhanSu` | `nvarchar(100)` | No |
| `@ThongTinCaNhanREF` | `nvarchar(400)` | No |
| `@MaSoThue` | `nvarchar(100)` | No |
| `@NgayBatDauLamViec` | `datetime(8)` | No |
| `@NgayNghiViec` | `datetime(8)` | No |
| `@ImageFileName` | `nvarchar(400)` | No |
| `@ImageFIleNameEncode` | `nvarchar(400)` | No |
| `@BiDanh` | `nvarchar(100)` | No |
| `@NoiSinh` | `nvarchar(400)` | No |
| `@NguyenQuan` | `nvarchar(8000)` | No |
| `@HoKhauThuongTru` | `nvarchar(8000)` | No |
| `@NoiOHienNay` | `nvarchar(8000)` | No |
| `@DanToc` | `nvarchar(100)` | No |
| `@TonGiao` | `nvarchar(100)` | No |
| `@TrinhDoVanHoa` | `nvarchar(100)` | No |
| `@NgoaiNgu` | `nvarchar(100)` | No |
| `@QuaTrinhBanThan` | `nvarchar(8000)` | No |
| `@CvFileName` | `nvarchar(400)` | No |
| `@CvFIleNameEncode` | `nvarchar(400)` | No |
| `@Code` | `nvarchar(100)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
| `@Active` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(2)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(2)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_InsertNhanSuSoYeuLyLich]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertNhanSuSoYeuLyLich]
	@NhanSuSoYeuLyLichID int,
	@MaNhanSu nvarchar(50),
	@ThongTinCaNhanREF nvarchar(200),
	@MaSoThue nvarchar(50),
	@NgayBatDauLamViec datetime,
	@NgayNghiViec datetime,
	@ImageFileName nvarchar(200),
	@ImageFIleNameEncode nvarchar(200),
	@BiDanh nvarchar(50),
	@NoiSinh nvarchar(200),
	@NguyenQuan nvarchar(4000),
	@HoKhauThuongTru nvarchar(4000),
	@NoiOHienNay nvarchar(4000),
	@DanToc nvarchar(50),
	@TonGiao nvarchar(50),
	@TrinhDoVanHoa nvarchar(50),
	@NgoaiNgu nvarchar(50),
	@QuaTrinhBanThan nvarchar(4000),
	@CvFileName nvarchar(200),
	@CvFIleNameEncode nvarchar(200),
	@Code nvarchar(50),
	@GhiChu nvarchar(4000),
	@Active int,
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

INSERT INTO [dbo].[NhanSuSoYeuLyLich] (
	[NhanSuSoYeuLyLichID],
	[MaNhanSu],
	[ThongTinCaNhanREF],
	[MaSoThue],
	[NgayBatDauLamViec],
	[NgayNghiViec],
	[ImageFileName],
	[ImageFIleNameEncode],
	[BiDanh],
	[NoiSinh],
	[NguyenQuan],
	[HoKhauThuongTru],
	[NoiOHienNay],
	[DanToc],
	[TonGiao],
	[TrinhDoVanHoa],
	[NgoaiNgu],
	[QuaTrinhBanThan],
	[CvFileName],
	[CvFIleNameEncode],
	[Code],
	[GhiChu],
	[Active],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
) VALUES (
	@NhanSuSoYeuLyLichID,
	@MaNhanSu,
	@ThongTinCaNhanREF,
	@MaSoThue,
	@NgayBatDauLamViec,
	@NgayNghiViec,
	@ImageFileName,
	@ImageFIleNameEncode,
	@BiDanh,
	@NoiSinh,
	@NguyenQuan,
	@HoKhauThuongTru,
	@NoiOHienNay,
	@DanToc,
	@TonGiao,
	@TrinhDoVanHoa,
	@NgoaiNgu,
	@QuaTrinhBanThan,
	@CvFileName,
	@CvFIleNameEncode,
	@Code,
	@GhiChu,
	@Active,
	@CreatedBy,
	@CreatedAt,
	@LastModifiedBy,
	@LastModifiedAt,
	@DeletedStatus,
	@PrintStatus,
	@RecordStatus
)

--endregion


```
