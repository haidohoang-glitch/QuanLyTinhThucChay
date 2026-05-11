# Stored Procedure: `sp_kiemtrachotsoB8`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-17 17:46:00.287000
- **Ngày sửa cuối**: 2026-03-17 17:46:00.287000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `date(3)` | No |
| `@NgayKetThuc` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.sp_kiemtrachotsoB8
    @NgayBatDau DATE,
    @NgayKetThuc DATE
AS
BEGIN
    SET NOCOUNT ON;

    -----------------------------------------
    -- 1. Chuẩn bị bảng hợp đồng
    -----------------------------------------
    PRINT N'--- B8.1: Load bảng hợp đồng ---'
    EXEC CheckThucChayVuotHopDong_TableHopDong

    -----------------------------------------
    -- 2. Tạo bảng ThucChayDaTinh
    -----------------------------------------
    PRINT N'--- B8.2: Load bảng Thực Chạy ---'
    EXEC CheckThucChayVuotHopDong_TableTCDT 
        @NgayBatDau, @NgayKetThuc

    -----------------------------------------
    -- 3. Check vượt theo từng loại
    -----------------------------------------
    PRINT N'--- B8.3: Check vượt hợp đồng ---'

    -- 1: Vượt theo hợp đồng
    EXEC dbo.CheckThucChayVuotHopDong_v2 @NgayKetThuc, 1

    -- 2: Vượt theo phân bổ
    EXEC dbo.CheckThucChayVuotHopDong_v2 @NgayKetThuc, 2

    -- 42: Admatic
    EXEC dbo.CheckThucChayVuotHopDong_v2 @NgayKetThuc, 42

    -- 733: Branding nhiều SP
    EXEC dbo.CheckThucChayVuotHopDong_v2 @NgayKetThuc, 733

    -- 13: Mua ngoài
    EXEC dbo.CheckThucChayVuotHopDong_v2 @NgayKetThuc, 13

    -- 3: Inventory
    EXEC dbo.CheckThucChayVuotHopDong_v2 @NgayKetThuc, 3

    -- Các nhóm đặc biệt
    EXEC dbo.CheckThucChayVuotHopDong_v2 @NgayKetThuc, 141
    EXEC dbo.CheckThucChayVuotHopDong_v2 @NgayKetThuc, 637
    EXEC dbo.CheckThucChayVuotHopDong_v2 @NgayKetThuc, 1412

END

```
