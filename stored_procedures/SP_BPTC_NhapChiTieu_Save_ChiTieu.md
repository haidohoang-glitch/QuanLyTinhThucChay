# Stored Procedure: `BPTC_NhapChiTieu_Save_ChiTieu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.220000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.220000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NguoiLog` | `nvarchar(510)` | No |
| `@LoaiLog` | `int(4)` | No |
| `@Values` | `BPTC_NhapChiTieu_ThongTinChiTieu_Type` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_NhapChiTieu_Save_ChiTieu]
    (
      @NguoiLog NVARCHAR(255) ,
      @LoaiLog INT ,      
      @Values BPTC_NhapChiTieu_ThongTinChiTieu_Type READONLY
    )
AS 
    BEGIN	
		
        SELECT  *
        INTO    #T
        FROM    @Values
        WHERE	ChiTieuID > 0
        	
        UPDATE  dbo.ThongTinChiTieu
        SET     DoanhSoChiTieu = T1.DoanhSoChiTieu
        FROM    dbo.ThongTinChiTieu T
                INNER JOIN #T T1 ON T.ThongTinChiTieuID = T1.ChiTieuID
                
        INSERT  INTO dbo.ThongTinChiTieuLog
                ( 
			      ChiTieuBoPhan ,
                  DmChiTieuBoPhanREF ,
                  LevelChiTieu ,
                  ThoiGianBatDau ,
                  ThoiGianKetThuc ,
                  DoanhSoChiTieu ,
                  LoaiTien ,
                  TenLoaiTien ,
                  NguoiDangKy ,
                  NguoiXacNhan ,
                  GhiChu ,
                  ThongTinChiTieuREF ,
                  LoaiLog ,
                  NguoiLog ,
                  NgayLog ,
                  CreatedBy ,
                  CreatedAt ,
                  LastModifiedBy ,
                  LastModifiedAt ,
                  DeleteStatus ,
                  PrintStatus ,
                  RecordStatus		        
                )
                SELECT  ChiTieuBoPhan ,
                        DmChiTieuBoPhanREF ,
                        LevelChiTieu ,
                        ThoiGianBatDau ,
                        ThoiGianKetThuc ,
                        DoanhSoChiTieu ,
                        LoaiTien ,
                        TenLoaiTien ,
                        NguoiDangKy ,
                        NguoiXacNhan ,
                        GhiChu ,
                        ThongTinChiTieuID ,
                        @LoaiLog ,
                        @NguoiLog ,
                        GETDATE() ,
                        @NguoiLog ,
                        GETDATE() ,
                        @NguoiLog ,
                        GETDATE() ,
                        0 ,
                        0 ,
                        0
                FROM    dbo.ThongTinChiTieu
                WHERE   ThongTinChiTieuID IN ( SELECT   ChiTieuID
                                               FROM     #T )		          	             
		
        DROP TABLE #T        
	
    END



```
