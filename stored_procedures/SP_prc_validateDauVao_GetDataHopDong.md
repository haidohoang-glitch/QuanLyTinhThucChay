# Stored Procedure: `prc_validateDauVao_GetDataHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-10 11:47:18.140000
- **Ngày sửa cuối**: 2026-03-11 11:23:37.890000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngayThucHien` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[prc_validateDauVao_GetDataHopDong]
    @ngayThucHien DATE
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @tableKey NVARCHAR(100) = N'HopDong';
    DECLARE @maxLastModifiedTimeYesterday DATETIME;
    DECLARE @dateRunJob DATETIME = dbo.fnc_get_MaxThoiGianChayJob_SyncDauVao(@ngayThucHien, 'hop-dong');

    DECLARE @maxLastModifiedTime DATETIME;

    ------------------------------------------------
    -- Lấy mốc last modified hôm trước
    ------------------------------------------------
    SELECT @maxLastModifiedTimeYesterday = DATEADD(DAY,-1,MaxLastModifiedTime)
    FROM dbo.QLTC_KetQuaValidateDauVao_HopDong_ThucTreo
    WHERE CONVERT(DATE,NgayKiemTra) = DATEADD(DAY,-1,@ngayThucHien)
        AND IsDeleted = 0
        AND TableMapping_Key = @tableKey

    IF(@maxLastModifiedTimeYesterday IS NULL)
    BEGIN
        SET @maxLastModifiedTimeYesterday = DATEADD(DAY,-1,@ngayThucHien);
    END

    ------------------------------------------------
    -- Max last modified ở đích
    ------------------------------------------------
    SELECT @maxLastModifiedTime = MAX(LastModifiedAt)
    FROM ABM_Data_ThucChay.dbo.HopDong WITH(NOLOCK)
    WHERE (
            (LastModifiedAt >= @maxLastModifiedTimeYesterday AND LastModifiedAt <= @dateRunJob)
            OR
            (CreatedAt >= @maxLastModifiedTimeYesterday AND CreatedAt <= @dateRunJob)
          )
        AND ISNULL(TrangThaiHopDong,0) <> 0;

    ------------------------------------------------
    -- DATA NGUỒN
    ------------------------------------------------
    SELECT 
        'SOURCE' AS DataType,
        *
    FROM dbo.V_Contract
    WHERE (
            (LAST_MODIFIED_AT >= @maxLastModifiedTimeYesterday AND LAST_MODIFIED_AT <= @dateRunJob)
            OR
            (CREATED_AT >= @maxLastModifiedTimeYesterday AND CREATED_AT <= @dateRunJob)
          );

    ------------------------------------------------
    -- DATA ĐÍCH
    ------------------------------------------------
    SELECT 
        'TARGET' AS DataType,
        *
    FROM ABM_Data_ThucChay.dbo.HopDong WITH(NOLOCK)
    WHERE (
            (LastModifiedAt >= @maxLastModifiedTimeYesterday AND LastModifiedAt <= @dateRunJob)
            OR
            (CreatedAt >= @maxLastModifiedTimeYesterday AND CreatedAt <= @dateRunJob)
          )
        AND ISNULL(TrangThaiHopDong,0) <> 0;

END

```
