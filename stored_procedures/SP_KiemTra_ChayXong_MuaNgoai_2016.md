# Stored Procedure: `KiemTra_ChayXong_MuaNgoai_2016`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-29 18:21:35.790000
- **Ngày sửa cuối**: 2016-11-29 18:21:35.790000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROC [KiemTra_ChayXong_MuaNgoai_2016]
AS 
BEGIN
SELECT
	TC.SoHopDong,
	TC.TenHTQC,
	TC.DMSanPhamREF,
	TC.[Tên sản phẩm],
	TC.thanhtienhd,
	TC.ThanhTienThucChay,
	TC.ThanhTienThucChay2016,
	TC.[Trang thai chay]
FROM dbo.['ThucChay2016_01012611']  TC

WHERE (DmHinhThucQuangCao=13 OR DmLoaiBannerREF=18)
AND thanhtienthucchay=thanhtienhd
ORDER BY SoHopDong
END



```
