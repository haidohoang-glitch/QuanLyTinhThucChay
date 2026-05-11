# Stored Procedure: `prc_asd_CheckThongTinDauVao_Get`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-03-24 10:54:10.003000
- **Ngày sửa cuối**: 2017-05-09 15:15:22.013000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@fromDate` | `datetime(8)` | No |
| `@toDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--SELECT * FROM dbo.CheckThongTinDauVao

--SELECT * FROM Check_DuLieuDauVaoSanPham

--SELECT * FROM Check_ThongTinDauRaSanPham;

CREATE PROCEDURE dbo.CheckThongTinDauVao_Get
	@fromDate datetime,
	@toDate datetime
AS
BEGIN
	Select distinct ST2.DoiTuong,ST2.LoaiVanDe,ST2.ThoiGianLog, 
    substring(
        (
            Select ', '+ CONVERT(VARCHAR(15), ST1.DoiTuongID)  AS [text()]
            From dbo.CheckThongTinDauVao ST1
            Where ST1.DoiTuong = ST2.DoiTuong AND st1.LoaiVanDe = st2.LoaiVanDe AND st1.ThoiGianLog=st2.ThoiGianLog
            ORDER BY ST1.DoiTuongID
            For XML PATH ('')
        ), 2, 1000) DoiTuongId
From dbo.CheckThongTinDauVao ST2
	WHERE CONVERT(VARCHAR(10), ST2.ThoiGianLog, 102) 
		BETWEEN CONVERT(VARCHAR(10), @fromDate, 102) AND CONVERT(VARCHAR(10), @toDate, 102)

	ORDER BY ST2.ThoiGianLog DESC
    
END

```
